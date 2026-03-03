from setuptools import find_packages, setup

package_name = 'altay_kontrol'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='muhammetbilal',
    maintainer_email='muhammetbilal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'ilk_node = altay_kontrol.ilk_node:main',
            'dron_merkezi = altay_kontrol.dron_merkezi:main',
            'yer_istasyonu = altay_kontrol.yer_istasyonu:main',
            'kamera_node = altay_kontrol.kamera_node:main',
            'karar_node = altay_kontrol.karar_node:main',
        ],
    },
)
