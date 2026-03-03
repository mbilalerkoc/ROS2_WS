import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math

class KararNode(Node):
    def __init__(self):
        super().__init__('karar_node')
        self.subscription = self.create_subscription(String, '/tespit_verileri', self.karar_callback, 10)
        

        self.merkez_x = 320.0
        self.merkez_y = 240.0
        self.hata_esigi = 30.0 

    def karar_callback(self, msg):
        parcalar = msg.data.split('|')
        label = parcalar[0]
        tx = float(parcalar[1])
        ty = float(parcalar[2])


        mesafe = math.sqrt((tx - self.merkez_x)**2 + (ty - self.merkez_y)**2) #uzaklık hesaplama

        if mesafe < self.hata_esigi:
            self.get_logger().info(f'HEDEF MERKEZLENDİ! Mesafe: {mesafe:.2f} px. BIRAKMAYA HAZIR!')

        else:
            self.get_logger().info(f'Takip ediliyor... Mesafe: {mesafe:.2f} px.')

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(KararNode())
    rclpy.shutdown()