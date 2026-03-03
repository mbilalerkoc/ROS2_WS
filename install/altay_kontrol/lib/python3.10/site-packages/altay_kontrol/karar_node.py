import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math

class KararNode(Node):
    def __init__(self):
        super().__init__('karar_node')
        self.subscription = self.create_subscription(String, '/tespit_verileri', self.karar_callback, 10)
        
        # Görüntü merkezi (Örn: 640x480 video için)
        self.merkez_x = 320.0
        self.merkez_y = 240.0
        self.hata_esigi = 30.0 # 30 piksellik bir tolerans tanıyalım

    def karar_callback(self, msg):
        # Gelen veri formatı: "HEDEF_KARE|345.2|210.5"
        parcalar = msg.data.split('|')
        label = parcalar[0]
        tx = float(parcalar[1])
        ty = float(parcalar[2])

        # Öklid Mesafesi Hesaplama (d)
        mesafe = math.sqrt((tx - self.merkez_x)**2 + (ty - self.merkez_y)**2)

        if mesafe < self.hata_esigi:
            self.get_logger().info(f'🎯 HEDEF MERKEZLENDİ! Mesafe: {mesafe:.2f} px. BIRAKMAYA HAZIR!')
            # Burada ileride MAVROS/PX4'e "servo aç" komutu göndereceğiz
        else:
            self.get_logger().info(f'🔍 Takip ediliyor... Mesafe: {mesafe:.2f} px.')

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(KararNode())
    rclpy.shutdown()