import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class YerIstasyonu(Node):
    def __init__(self):
        super().__init__('yer_istasyonu')
        # Aynı kanalı dinlemeye başlıyoruz
        self.subscription = self.create_subscription(
            String, '/dron_telemetri', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Veri Alındı: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = YerIstasyonu()
    rclpy.spin(node)
    rclpy.shutdown()