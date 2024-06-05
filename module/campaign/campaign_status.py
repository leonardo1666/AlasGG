<<<<<<< HEAD
import datetime
=======
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
import re

import cv2
import numpy as np

from module.base.timer import Timer
<<<<<<< HEAD
from module.campaign.assets import OCR_EVENT_PT, OCR_COIN, OCR_OIL, OCR_COIN_LIMIT, OCR_OIL_LIMIT, OCR_OIL_CHECK
from module.base.utils import color_similar, get_color
from module.logger import logger
from module.ocr.ocr import Digit, Ocr
from module.ui.ui import UI
from module.log_res.log_res import LogRes
=======
from module.base.utils import color_similar, get_color
from module.campaign.assets import OCR_COIN, OCR_EVENT_PT, OCR_OIL, OCR_OIL_CHECK
from module.logger import logger
from module.ocr.ocr import Digit, Ocr
from module.ui.ui import UI

OCR_COIN = Digit(OCR_COIN, name='OCR_COIN', letter=(239, 239, 239), threshold=128)
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0


class PtOcr(Ocr):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, lang='azur_lane', alphabet='X0123456789', **kwargs)

    def pre_process(self, image):
        """
        Args:
            image (np.ndarray): Shape (height, width, channel)

        Returns:
            np.ndarray: Shape (width, height)
        """
        # Use MAX(r, g, b)
        r, g, b = cv2.split(cv2.subtract((255, 255, 255, 0), image))
        image = cv2.min(cv2.min(r, g), b)
        # Remove background, 0-192 => 0-255
        image = cv2.multiply(image, 255 / 192)

        return image.astype(np.uint8)


OCR_PT = PtOcr(OCR_EVENT_PT)


class CampaignStatus(UI):
<<<<<<< HEAD
    def get_event_pt(self, update=False):
=======
    def get_event_pt(self):
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
        """
        Returns:
            int: PT amount, or 0 if unable to parse
        """
        pt = OCR_PT.ocr(self.device.image)

        res = re.search(r'X(\d+)', pt)
        if res:
            pt = int(res.group(1))
            logger.attr('Event_PT', pt)
<<<<<<< HEAD
            LogRes(self.config).Pt = pt
        else:
            logger.warning(f'Invalid pt result: {pt}')
            pt = 0
        if update:
            self.config.update()
        return pt

    def get_coin(self, skip_first_screenshot=True, update=False):
=======
            return pt
        else:
            logger.warning(f'Invalid pt result: {pt}')
            return 0

    def get_coin(self, skip_first_screenshot=True):
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
        """
        Returns:
            int: Coin amount
        """
<<<<<<< HEAD
        _coin = {}
=======
        amount = 0
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
        timeout = Timer(1, count=2).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if timeout.reached():
                logger.warning('Get coin timeout')
                break

<<<<<<< HEAD
            _coin = {
                'Value': self._get_num(OCR_COIN, 'OCR_COIN'),
                'Limit': self._get_num(OCR_COIN_LIMIT, 'OCR_COIN_LIMIT')
            }
            if _coin['Value'] >= 100:
                break
        LogRes(self.config).Coin = _coin
        if update:
            self.config.update()

        return _coin['Value']
=======
            amount = OCR_COIN.ocr(self.device.image)
            if amount >= 100:
                break

        return amount
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0

    def _get_oil(self):
        # Update offset
        _ = self.appear(OCR_OIL_CHECK)

        color = get_color(self.device.image, OCR_OIL_CHECK.button)
        if color_similar(color, OCR_OIL_CHECK.color):
            # Original color
            ocr = Digit(OCR_OIL, name='OCR_OIL', letter=(247, 247, 247), threshold=128)
        elif color_similar(color, (59, 59, 64)):
            # With black overlay
            ocr = Digit(OCR_OIL, name='OCR_OIL', letter=(165, 165, 165), threshold=128)
        else:
            logger.warning(f'Unexpected OCR_OIL_CHECK color')
            ocr = Digit(OCR_OIL, name='OCR_OIL', letter=(247, 247, 247), threshold=128)

        return ocr.ocr(self.device.image)

<<<<<<< HEAD
    def _get_num(self, _button, name):
        # Update offset
        _ = self.appear(OCR_OIL_CHECK)

        color = get_color(self.device.image, OCR_OIL_CHECK.button)
        if color_similar(color, OCR_OIL_CHECK.color):
            # Original color
            ocr = Digit(_button, name=name, letter=(247, 247, 247), threshold=128)
        elif color_similar(color, (59, 59, 64)):
            # With black overlay
            ocr = Digit(_button, name=name, letter=(165, 165, 165), threshold=128)
        else:
            logger.warning(f'Unexpected OCR_OIL_CHECK color')
            ocr = Digit(_button, name=name, letter=(247, 247, 247), threshold=128)

        return ocr.ocr(self.device.image)

    def get_oil(self, skip_first_screenshot=True, update=False):
=======
    def get_oil(self, skip_first_screenshot=True):
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
        """
        Returns:
            int: Oil amount
        """
<<<<<<< HEAD
        _oil = {}
=======
        amount = 0
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
        timeout = Timer(1, count=2).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

<<<<<<< HEAD
            if not self.appear(OCR_OIL_CHECK, offset=(10, 2)):
                logger.info('No oil icon')
                self.device.sleep(1)

=======
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
            if timeout.reached():
                logger.warning('Get oil timeout')
                break

<<<<<<< HEAD
            _oil = {
                'Value': self._get_num(OCR_OIL, 'OCR_OIL'),
                'Limit': self._get_num(OCR_OIL_LIMIT, 'OCR_OIL_LIMIT')
            }
            if _oil['Value'] >= 100:
                break
        LogRes(self.config).Oil = _oil
        if update:
            self.config.update()

        return _oil['Value']
=======
            if not self.appear(OCR_OIL_CHECK, offset=(10, 2)):
                logger.info('No oil icon')
                continue

            amount = self._get_oil()
            if amount >= 100:
                break

        return amount
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0

    def is_balancer_task(self):
        """
        Returns:
             bool: If is event task but not daily event task
        """
        tasks = [
            'Event',
            'Event2',
<<<<<<< HEAD
            'Event3',
            'coalition',
            'coalition_sp',
=======
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
            'Raid',
            'GemsFarming',
        ]
        command = self.config.Scheduler_Command
        if command in tasks:
            if self.config.Campaign_Event == 'campaign_main':
                return False
            else:
                return True
        else:
            return False
