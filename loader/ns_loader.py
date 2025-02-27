from datetime import datetime

import requests

from .base_loader import BaseLoader, LoadError
from .config import NS_CLAENDAR_URL, NS_CLIENT_ID, NS_GRANT_TYPE, NS_TOKEN_URL


class NSLoader(BaseLoader):
    unit = "mins"

    def __init__(self, from_year, to_year, **kwargs):
        super().__init__(from_year, to_year)
        self.session_token = kwargs.get("session_token", "")
        self.device_id = kwargs.get("device_id", "")
        self.headers = {
            "x-moon-os-language": "en-US",
            "x-moon-app-language": "en-US",
            "authorization": "",
            "x-moon-app-internal-version": "293",
            "x-moon-app-display-version": "1.14.0",
            "x-moon-os": "IOS",
            "accept-encoding": "gzip;q=1.0, compress;q=0.5",
            "accept-language": "en-US;q=1.0",
            "user-agent": "moon_ios/1.14.0 (com.nintendo.znma; build:293; iOS 14.2.0) "
            "Alamofire/4.8.2",
            "x-moon-timezone": "America/Los_Angeles",
        }
        self.s = requests.Session()

    @classmethod
    def add_loader_arguments(cls, parser):
        parser.add_argument(
            "--device_id",
            dest="device_id",
            type=str,
            required=True,
            help="",
        )
        parser.add_argument(
            "--session_token",
            dest="session_token",
            type=str,
            required=True,
            help="",
        )

    def _make_access_headers(self):
        r = self.s.post(
            NS_TOKEN_URL,
            data={
                "session_token": self.session_token,
                "client_id": NS_CLIENT_ID,
                "grant_type": NS_GRANT_TYPE,
            },
        )
        if not r.ok:
            raise LoadError("can not get ns access token")
        access = r.json()
        self.headers["authorization"] = (
            access["token_type"] + " " + access["access_token"]
        )

    def get_api_data(self):
        self._make_access_headers()
        month_list = self.make_month_list()
        data_list = []
        for m in month_list:
            # no data for this month for ns
            if m.month == datetime.now().month:
                continue
            r = self.s.get(
                NS_CLAENDAR_URL.format(
                    device_id=self.device_id,
                    # ns month format
                    month=m.to_date_string()[:7],
                ),
                headers=self.headers,
            )
            if not r.ok:
                print(f"Get ns calendar api failed {str(r.text)}")
            try:
                data_list.extend(list(r.json()["dailySummaries"].values()))
            except Exception:
                # just pass for now
                pass
        return data_list

    def make_track_dict(self):
        data_list = self.get_api_data()
        for d in data_list:
            number = d.get("playingTime", 0)
            if number:
                minutes = int(number / 60)
                self.number_by_date_dict[d["date"]] = minutes
                self.number_list.append(minutes)

    def get_all_track_data(self):
        self.make_track_dict()
        self.make_special_number()
        return self.number_by_date_dict, self.year_list
