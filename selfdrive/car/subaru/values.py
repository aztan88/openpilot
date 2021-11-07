# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  STEER_MAX = 2047              # max_steer 4095
  STEER_STEP = 2                # how often we update the steer cmd
  STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
  STEER_DELTA_DOWN = 70         # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 10  # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1       # from dbc

  RPM_MIN = 0                   # min cruise_rpm
  RPM_MAX = 3200                # max cruise_rpm
  RPM_BASE = 600                # cruise_rpm idle, from stock drive
  RPM_SCALE = 85                # cruise_rpm, from testing

  THROTTLE_MIN = 0              # min cruise_throttle
  THROTTLE_MAX = 3400           # max cruise_throttle
  THROTTLE_BASE = 1810          # cruise_throttle, from stock drive
  THROTTLE_SCALE = 85           # from testing

  RPM_DELTA_UP = 50
  RPM_DELTA_DOWN = 50

  THROTTLE_DELTA_UP = 50
  THROTTLE_DELTA_DOWN = 50

  BRAKE_MIN = 0
  BRAKE_MAX = 400
  BRAKE_SCALE = 150             # from testing

class CAR:
  ASCENT = "SUBARU ASCENT LIMITED 2019"
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  FORESTER = "SUBARU FORESTER 2019"
  CROSSTREK = "SUBARU CROSSTREK LIMITED 2018"
  FORESTER_PREGLOBAL = "SUBARU FORESTER 2017 - 2018"
  LEGACY_PREGLOBAL = "SUBARU LEGACY 2015 - 2018"
  OUTBACK_PREGLOBAL = "SUBARU OUTBACK 2015 - 2017"
  OUTBACK_PREGLOBAL_2018 = "SUBARU OUTBACK 2018 - 2019"

FINGERPRINTS = {
  CAR.ASCENT: [{
  # SUBARU ASCENT LIMITED 2019
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1722: 8, 1743: 8, 1759: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  }],
  CAR.IMPREZA: [{
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 816: 8, 826: 8, 827: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  }],
  CAR.CROSSTREK: [{
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  }],
  CAR.FORESTER: [{
  # Forester 2019-2020
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 961: 8, 984: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1651: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1698: 8, 1722: 8, 1743: 8, 1759: 8, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  }],
  CAR.OUTBACK_PREGLOBAL: [{
  # OUTBACK PREMIUM 2.5i 2015
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 346: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1786: 5, 1882: 8, 2015: 8, 2016: 8, 2024: 8, 604: 8, 885: 8, 1788: 8, 316: 8, 1614: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1743: 8, 1785: 5, 1787: 5
  },
  # OUTBACK PREMIUM 3.6i 2015
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 644: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 977: 8, 1632: 8, 1745: 8, 1779: 8, 1786: 5
  },
  # OUTBACK LIMITED 2.5i 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8
  }],
  CAR.OUTBACK_PREGLOBAL_2018: [{
  # OUTBACK LIMITED 3.6R 2019
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 644: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 2, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1736: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1862: 8, 1870: 8, 1920: 8, 1927: 8, 1928: 8, 1935: 8, 1968: 8, 1976: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.FORESTER_PREGLOBAL: [{
  # FORESTER PREMIUM 2.5i 2017
    2: 8, 112: 8, 117: 8, 128: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 340: 7, 342: 8, 352: 8, 353: 8, 354: 8, 355: 8, 356: 8, 554: 8, 604: 8, 640: 8, 641: 8, 642: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 886: 1, 888: 8, 977: 8, 1398: 8, 1632: 8, 1743: 8, 1744: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 1882: 8, 1895: 8, 1903: 8, 1986: 8, 1994: 8, 2015: 8, 2016: 8, 2024: 8, 644:8, 890:8, 1736:8
  }],
  CAR.LEGACY_PREGLOBAL: [{
  # LEGACY 2.5i 2017
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1632: 8, 1640: 8, 1736: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 644: 8
  },
  # LEGACY 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 392: 8, 604: 8, 640: 8, 642: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1778: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  },
  # LEGACY 2018
  {
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 604: 8, 640: 8, 642: 8, 805: 8, 864: 8, 865: 8, 866: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1640: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1743: 8, 1745: 8, 1785: 5, 1786: 5, 1787: 5, 1788: 8, 2015: 8, 2016: 8, 2024: 8
  }],
}

FW_VERSIONS = {
  CAR.ASCENT: {
    # 2019 Ascent UDM
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa5 \x19\x02\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x85\xc0\xd0\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xb9\x1f@ \x10',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbb,\xa0t\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\x00\xfe\xf7\x00\x00',
    ],
  },
  CAR.CROSSTREK: {
    # 2018 Crosstrek EDM
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\x7a\x94\x3f\x90\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'\x7a\xc0\x0c\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00\x64\xb5\x1f\x40\x20\x0e',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xaa\x61\x66\x73\x07',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe3\xe5\x46\x31\x00',
    ],
  },
  CAR.IMPREZA: {
    # 2018 Impreza ADM
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [
      b'\xa2 \x185\x00',
    ],
    (Ecu.eps, 0x746, None): [
      b'z\xc0\b\x00',
    ],
    (Ecu.fwdCamera, 0x787, None): [
      b'\x00\x00d\xdc\x1f@ \x0e',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\xbeacr\a',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xe4\xe5\x061\x00',
    ],
  },
}

STEER_THRESHOLD = {
  CAR.ASCENT: 80,
  CAR.IMPREZA: 80,
  CAR.FORESTER: 80,
  CAR.CROSSTREK: 80,
  CAR.FORESTER_PREGLOBAL: 75,
  CAR.LEGACY_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL_2018: 75,
}

DBC = {
  CAR.ASCENT: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER: dbc_dict('subaru_global_2017_generated', None),
  CAR.CROSSTREK: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.LEGACY_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
}

PREGLOBAL_CARS = [CAR.FORESTER_PREGLOBAL, CAR.LEGACY_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018]
