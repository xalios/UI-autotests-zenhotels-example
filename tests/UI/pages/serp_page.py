from selene import browser


class Serp:
    def __init__(self):
        self.url = "https://www.zenhotels.com/hotel/russia/"
        # Result title
        self.result_title = browser.element('[class="zenserpresult-header"]')

        # Hotel cards
        self.price_notice = browser.all('[class="zen-hotelcard-rate-price-notice"]')

    def open(self, region, checkin_date, checkout_date, guests):
        browser.open(
            f'{self.url}{region}/?dates={checkin_date}-{checkout_date}&guests={guests}'
        )


