# GitHubPoster
Make everything a GitHub svg poster and [skyline](https://skyline.github.com/)!

##  `svg` in `README` emamples

![](https://github.com/yihong0618/GitHubPoster/blob/main/examples/twitter.svg)
![](https://github.com/yihong0618/GitHubPoster/blob/main/examples/shanbay.svg)

## Support
- **[Strava](#strava)**
- **[Nintendo Switch](#ns)**
- **[GPX](#GPX)**
- **[Duolingo](#duolingo)**
- **[Issue](#Issue)**
- **[Twitter](#Twitter)**
- **[YouTube](#Youtube)**
- **[Bilibili](#Bilibili)**
- **[GitHub](#GitHub)**
- **[GitLab](#GitLab)**
- **[Kindle](#Kindle)**
- **[WakaTime](#WakaTime)**
- **[Dota2](#Dota2)**

## Download
```
git clone https://github.com/yihong0618/GitHubPoster.git
```
## Install(Python3.6+)
```
pip3 install -r requirements.txt
```

## Use

- Different types are used as specified below
- You can specify a year such as --year 2021, (default) or a year range 2012-2021
- The generated svg is in `OUT_FOLDER`, named with type (for now)
- By default, the number of different colors is automatically generated (special colors), you can also specify the color: --special-number1 10 -- special_number2 20
- You can also specify the color: --special-color1 pink --special-color2 '#33C6A4'
- Other parameters can be found with `python cli.py <type> --help`
- you can add animation, --with-animation (add GOGOGO animation), you can control the animation time --animation-time 14 (default is 10s)
- you can save skyline `stl` file --with-skyline (default skyline year is to_year)


### GPX

<details>
<summary>Make your <code>GPX</code> GitHub poster</summary>
<br>

mv gpx files to `GPX_FOLDER` then run the code
```
python3 cli.py gpx --dir ~/blog/GPX_OUT/ --year 2013-2021
```
</details>

### Strava

<details>
<summary>Make your <code>Strava</code> GitHub poster</summary>

1. Sign in/Sign up [Strava](https://www.strava.com/) account
2. Open after successful Signin [Strava Developers](http://developers.strava.com) -> [Create & Manage Your App](https://strava.com/settings/api)

3. Create `My API Application`: Enter the following information

<br>

![My API Application](https://raw.githubusercontent.com/shaonianche/gallery/master/running_page/strava_settings_api.png)
Created successfully：

<br>

![](https://raw.githubusercontent.com/shaonianche/gallery/master/running_page/created_successfully_1.png)

4. Use the link below to request all permissions: Replace `${your_id}` in the link with `My API Application` `Client ID`
```
https://www.strava.com/oauth/authorize?client_id=${your_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all,profile:read_all,activity:read_all,profile:write,activity:write
```
![get_all_permissions](https://raw.githubusercontent.com/shaonianche/gallery/master/running_page/get_all_permissions.png)

5. Get the `code` value in the link

<br>

example：
```
http://localhost/exchange_token?state=&code=1dab37edd9970971fb502c9efdd087f4f3471e6e&scope=read,activity:write,activity:read_all,profile:write,profile:read_all,read_all
```
`code` value：
```
1dab37edd9970971fb502c9efdd087f4f3471e6
```
![get_code](https://raw.githubusercontent.com/shaonianche/gallery/master/running_page/get_code.png)

6. Use `Client_id`、`Client_secret`、`Code` get `refresch_token`: Execute in `Terminal/iTerm`
```
curl -X POST https://www.strava.com/oauth/token \
-F client_id=${Your Client ID} \
-F client_secret=${Your Client Secret} \
-F code=${Your Code} \
-F grant_type=authorization_code
```
example：
```
curl -X POST https://www.strava.com/oauth/token \
-F client_id=12345 \
-F client_secret=b21******d0bfb377998ed1ac3b0 \
-F code=d09******b58abface48003 \
-F grant_type=authorization_code
```
![get_refresch_token](https://raw.githubusercontent.com/shaonianche/gallery/master/running_page/get_refresch_token.png)

```
python3 cli.py strava --client_id  ${client_id} --client_secret ${client_secret} --refresh_token ${refresh_token} --year 2012-2021}
```
</details>

### NS

<details>
<summary>Make your <code>Nintendo Switch</code> GitHub poster</summary>
<br>

From APP`(Nintendo Switch Parent Controls)` using `mitmproxy` to get the `session_token` and `devide _id`

```
python3 cli.py ns --session_token ${session_token} --device_id ${device_id} --year 2020-2021
```
</details>


### Duolingo

<details>
<summary>Make your <code>Duolingo</code> GitHub poster</summary>
<br>

Find your `duolingo id`, F12 from `XHR`
![image](https://user-images.githubusercontent.com/15976103/116336188-baad7000-a80a-11eb-80d7-033d4bf0f260.png)


```
python3 cli.py duolingo --user_name ${user_id} --year 2015-2021
```
</details>

### Issue

<details>
<summary>Make your <code>Issue</code> GitHub poster</summary>
<br>

Like my issue [issue](https://github.com/yihong0618/2021/issues/5)

```
python3 cli.py issue --issue_number ${issue_number} --repo_name ${repo_name} --token ${github_token}
```
</details>

### LeetCode

<details>
<summary>Make your <code>LeetCode</code> GitHub poster</summary>
<br>

Find your `LeetCode Cookie`

```
python3 cli.py leetcode --cookie ${leetcode_cookie} --year 2019-2021
```

</details>

### Twitter

<details>
<summary>Make your <code>Twitter</code> GitHub poster</summary>
<br>

Find your `Twitter user_id` (in the url)

```
python3 cli.py twitter --user_name ${twitter_user_name} --year 2018-2021 --track-color '#1C9CEA'
```
</details>

### Youtube

<details>
<summary>Make your <code>YouTube</code> GitHub poster</summary>
<br>

Use Google [History Takeout](https://takeout.google.com/settings/takeout) to download `YouTube` history data，choose `json` format，mv `watch-history.json` to `IN-FOLDER` then run the code

```
python3 cli.py youtube --year 2015-2021
```
</details>

### Bilibili

<details>
<summary>Make your <code>Bilibili</code> GitHub poster</summary>
<br>

Find your `Bilibili (XHR) cookie`

```
python3 cli.py bilibili --cookie "${bilibili-cookie}"
```
</details>

### GitHub

<details>
<summary>Make your <code>GitHub</code> GitHub poster</summary>
<br>

Get your `GitHub Name` (in the url)

```
python3 cli.py github --user_name "${github_user_name}" --with-skyline
```
</details>

### GitLab

<details>
<summary>Make your <code>GitLab</code> GitLab poster</summary>
<br>

Get your `GitLab Name` (in the url)

```
python3 cli.py gitlab --user_name "${gitlab_user_name}"
```

For self-managed `GitLab`, specify the base url of your instance. You should use `_gitlab_session` from Cookies if sign in required.
s
```
python3 cli.py gitlab --user_name "${gitlab_user_name}" --base_url "https://your-gitlab.com" --session "${gitlab_session}"
```

</details>

### Kindle

<details>
<summary>Make your <code>Kindle</code> GitHub poster</summary>
<br>

Find your [Amazon](https://www.amazon.com/) Cookie

```
python3 cli.py kindle --cookie ${kindle_cookie} --year 2018-2021
```

</details>

### WakaTime

<details>
<summary>Make your <code>WakaTime</code> poster</summary>
<br>

Find your own `WakaTime API Key` at: [WakaTime API Key](https://wakatime.com/settings/api-key)

```
python cli.py wakatime --key="your_wakatime_api_key" --year 2019-2021
```

</details>

### Dota2

<details>
<summary>Make your <code>Dota2</code> poster</summary>
<br>

Find your `dota2_id`, eg：Dendi's ID `70388657`
Check your dota2_id(steamid32): https://steamid.xyz/.
Check your game data: https://api.opendota.com/api/players/{dota2_id}/matches.
more info: https://docs.opendota.com/#section/Introduction"


```
python cli.py dota2 --id="your dota2 id" --year 2017-2018
```

# Contribution

- Any Issues PR welcome.
- Any new loader welcome

Before submitting PR:
- Format Python code with `black` (`black .`)
- Format Python code with `isort` (`isort --profile black  **/*.py`)

# TODO

- [x] twitter
- [x] GitLab
- [x] GitHub
- [x] LeetCode
- [x] GitHub from issues
- [x] YouTube
- [x] Bilibili
- [x] GitHub Actions
- [x] Change all default color
- [x] Skyline
- [x] Dota2
- [ ] Loader doc
- [ ] pypi
- [x] test
- [x] English README

# GitHub Actions

1. fork or clone this repo
2. Change the secrets
3. Change the `type` in `yml` file

![image](https://user-images.githubusercontent.com/15976103/116517569-be6fee00-a901-11eb-9178-55df0c3301e3.png)
![image](https://user-images.githubusercontent.com/15976103/116517636-d21b5480-a901-11eb-90e7-8314404f5f59.png)

# Special thanks
- @[flopp](https://github.com/flopp) great repo [GpxTrackPoster](https://github.com/flopp/GpxTrackPoster)
- @[JasonkayZK](https://github.com/JasonkayZK) Wakatime loader
- @[shaonianche](https://github.com/shaonianche) Dota2 loader
- @[frostming](https://github.com/frostming) `CI` refator and some Actions code

# Support
Thanks is enough.
