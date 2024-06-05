<<<<<<< HEAD
from module.base.decorator import Config
=======
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
from module.shop.shop_core import CoreShop
from module.shop.shop_general import GeneralShop
from module.shop.shop_guild import GuildShop
from module.shop.shop_medal import MedalShop2
from module.shop.shop_merit import MeritShop
from module.shop.ui import ShopUI


class RewardShop(ShopUI):
    def run_frequent(self):
        # Munitions shops
        self.ui_goto_shop()

        self.shop_tab.set(main=self, left=2)
        self.shop_nav.set(main=self, upper=1)
        GeneralShop(self.config, self.device).run()

        self.config.task_delay(server_update=True)

<<<<<<< HEAD
    @Config.when(SERVER='tw')
    def run_once(self):
        # Munitions shops
        self.ui_goto_shop()

        self.shop_tab.set(main=self, left=2)
        self.shop_nav.set(main=self, upper=2)
        MeritShop(self.config, self.device).run()

        self.shop_tab.set(main=self, left=2)
        self.shop_nav.set(main=self, upper=3)
        GuildShop(self.config, self.device).run()

        # core monthly, medal, prototype
        self.shop_tab.set(main=self, left=1)
        self.shop_nav.set(main=self, upper=1)
        CoreShop(self.config, self.device).run()

        self.shop_tab.set(main=self, left=1)
        self.shop_nav.set(main=self, upper=2)
        MedalShop2(self.config, self.device).run()

        self.config.task_delay(server_update=True)

    @Config.when(SERVER=None)
=======
>>>>>>> 24aa3e00bd9af9a6a050df54c6a0cef959a9c6c0
    def run_once(self):
        # Munitions shops
        self.ui_goto_shop()

        self.shop_tab.set(main=self, left=2)
        self.shop_nav.set(main=self, upper=2)
        MeritShop(self.config, self.device).run()

        self.shop_tab.set(main=self, left=2)
        self.shop_nav.set(main=self, upper=3)
        GuildShop(self.config, self.device).run()

        # core limited, core monthly, medal, prototype
        self.shop_tab.set(main=self, left=1)
        self.shop_nav.set(main=self, upper=2)
        CoreShop(self.config, self.device).run()

        self.shop_tab.set(main=self, left=1)
        self.shop_nav.set(main=self, upper=3)
        MedalShop2(self.config, self.device).run()

        self.config.task_delay(server_update=True)
