import json
import string
from time import sleep

import requests


class DomainChecker:
    def __init__(self, tld):
        self.tld = tld
        self.check_url = "https://www.hosting.kr/domains?query={}"
        self.headers = {
            "content-type": "application/json",
            "x-requested-with": "XMLHttpRequest"
        }

    def check_target_domains(self, target_domains):
        found_domains = []
        for d in target_domains:
            if self.check(self.get_target_url(d)):
                found_domains.append(d)
            sleep(0.5)
        return target_domains

    def find_short_domain(self):
        for a in string.ascii_lowercase:
            for b in string.ascii_lowercase:
                target_domain = self.get_target_domain(a + b)
                target_url = self.get_target_url(target_domain)
                if self.check(target_url):
                    print(target_domain)
                sleep(0.5)

    def check(self, target_url):
        res = requests.get(target_url, headers=self.headers).json()
        return res['statusMsg'] == '등록가능'

    def get_target_domain(self, name):
        return "{}.{}".format(name, self.tld)

    def get_target_url(self, target_domain):
        return self.check_url.format(target_domain)


if __name__ == '__main__':
    target_domains = ['jslee.me']
    dc = DomainChecker("me")
    for d in target_domains:
        dc.check_target_domains(target_domains)
    # dc.find_short_domain()
