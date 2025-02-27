#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# some code from https://github.com/flopp/GpxTrackPoster

import argparse
import os

from github_poster import drawer, poster
from github_poster.utils import parse_years
from loader import (
    BilibiliLoader,
    CiChangLoader,
    Dota2Loader,
    DuolingoLoader,
    GitHubIssuesLoader,
    GitHubLoader,
    GitLabLoader,
    GPXLoader,
    KindleLoader,
    LeetcodeLoader,
    NSLoader,
    ShanBayLoader,
    StravaLoader,
    TwitterLoader,
    WakaTimeLoader,
    YouTubeLoader,
)
from skyline import Skyline

LOADER_DICT = {
    "duolingo": DuolingoLoader,
    "shanbay": ShanBayLoader,
    "strava": StravaLoader,
    "cichang": CiChangLoader,
    "ns": NSLoader,
    "gpx": GPXLoader,
    "issue": GitHubIssuesLoader,
    "leetcode": LeetcodeLoader,
    "twitter": TwitterLoader,
    "youtube": YouTubeLoader,
    "bilibili": BilibiliLoader,
    "github": GitHubLoader,
    "gitlab": GitLabLoader,
    "kindle": KindleLoader,
    "wakatime": WakaTimeLoader,
    "dota2": Dota2Loader,
}

OUT_FOLDER = os.path.join(os.getcwd(), "OUT_FOLDER")


def main():
    """Handle command line arguments and call other modules as needed."""
    p = poster.Poster()
    args_parser = argparse.ArgumentParser()
    subparser = args_parser.add_subparsers()
    for type_, loader in LOADER_DICT.items():
        parser = subparser.add_parser(name=type_)
        parser.set_defaults(type=type_, loader=loader)
        loader.add_arguments(parser)

    args = args_parser.parse_args()

    # we don't know issue content so use name
    p.title = (
        f"{args.me} " + str(args.type).upper() if args.type != "issue" else args.me
    )

    p.colors = {
        "background": args.background_color,
        "track": args.loader.track_color  # some type has default color
        or args.track_color,
        "special": args.special_color1,
        "special2": args.special_color2 or args.special_color,
        "text": args.text_color,
    }
    # set animate
    p.set_with_animation(args.with_animation)
    p.set_animation_time(args.animation_time)
    p.units = args.loader.unit
    from_year, to_year = parse_years(args.year)
    d = LOADER_DICT.get(args.type, "duolingo")(
        from_year, to_year, **dict(args._get_kwargs())
    )
    tracks, years = d.get_all_track_data()
    p.special_number = {
        "special_number1": d.special_number1,
        "special_number2": d.special_number2,
    }
    if args.special_number1:
        p.special_number["special_number1"] = args.special_number1
    if args.special_number2:
        p.special_number["special_number2"] = args.special_number2
    p.set_tracks(tracks, years)
    p.height = 35 + len(p.years) * 43
    if not os.path.exists(OUT_FOLDER):
        os.mkdir(OUT_FOLDER)
    p.draw(drawer.Drawer(p), os.path.join(OUT_FOLDER, str(args.type) + ".svg"))

    # generate skyline
    if args.with_skyline:
        if args.skyline_year:
            year = args.skyline_year
        else:
            year = years[-1]
        # filter data
        number_by_date_dict = {k: v for k, v in tracks.items() if k[:4] == str(year)}
        s = Skyline(
            os.path.join(OUT_FOLDER, f"{year}_{str(args.type)}" + ".stl"),
            year,
            args.type,
            number_by_date_dict,
        )
        s.make_skyline()


if __name__ == "__main__":
    main()
