from selene import browser


class HotelPage:
    def __init__(self):
        # Hotel title
        self.hotel_title = browser.element('[class="zen-roomspage-title-name"]')

