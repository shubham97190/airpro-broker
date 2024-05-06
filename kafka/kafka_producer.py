import logging
import time

import schedule
from confluent_kafka import Producer

logger = logging.getLogger(__name__)


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        logger.warning('Message delivery failed: {}'.format(msg))
    else:
        logger.info('Message delivered to {} {}'.format(msg.topic(), msg.partition()))


class AppKafkaProducer:

    def __init__(self, topic_name):
        self.producer = Producer({'bootstrap.servers': '0.0.0.0:9092',
                                  "linger.ms": "4000", "batch.size": "1000000"})
        self.topic = topic_name
        # self.trigger_scheduler()

    def send_message(self, message, headers):
        # Asynchronously produce a message. The delivery report callback will
        # be triggered from the call to poll() above, or flush() below, when the
        # message has been successfully delivered or failed permanently.
        self.producer.produce(self.topic, message, callback=None, headers=headers)
        # Wait for any outstanding messages to be delivered and delivery report
        # callbacks to be triggered.
        self.producer.poll(0)
        self.producer.flush()

    def a_poll(self):
        try:
            logger.info("Poll starting...")
            total = self.producer.flush()
            logger.info("Poll executed total Message in queue %s ", total)
        except Exception as e:
            # Handle the exception here
            print(f"An error occurred: {str(e)}")

    def trigger_scheduler(self):
        logger.info("Job Triggered")
        schedule.every(5).seconds.do(self.a_poll)
        while True:
            schedule.run_pending()
            time.sleep(1)
