from flet import *
import pyperclip


def main(page: Page):
    page.window_width = 300
    page.window_height = 740
    page.window_left = 0
    page.window_top = 0

    def tp(s):
        if rtype.value == "New Release":
            content.controls.clear()
            content.controls.append(Column(
                [Row([beatport, beatport_link]), Row([spotify, spotify_link]), Row([itunes, itunes_link]),
                 Row([youtube, youtube_link]), Row([soundcloud, soundcloud_link])]))
            page.window_height = 740
            itunes.value = True
            youtube.value = True
            soundcloud.value = True
            page.update()
        else:
            content.controls.clear()
            content.controls.append(Column([Row([beatport, beatport_link]), Row([spotify, spotify_link])]))
            itunes.value = False
            youtube.value = False
            soundcloud.value = False

            page.window_height = 540
            page.update()

    label = Dropdown(options=[
        dropdown.Option("Primavera Organica"),
        dropdown.Option("Nature Collections"),
        dropdown.Option("The Ocean Heaven")
    ], hint_text="Select Label")

    rtype = Dropdown(options=[
        dropdown.Option("New Release"),
        dropdown.Option("Pre Order")
    ], hint_text="Select Type", on_change=tp)

    img = TextField(label="Image Link")
    title = TextField(label="Release Title")
    artist = TextField(label="Artist")

    def beat(d):
        print(beatport_link.disabled)
        if not beatport.value:
            beatport_link.disabled = True
            page.update()
        else:
            beatport_link.disabled = False
            page.update()

    def spoty(d):
        if not spotify.value:
            spotify_link.disabled = True
            page.update()
        else:
            spotify_link.disabled = False
            page.update()

    def itus(d):
        if not itunes.value:
            itunes_link.disabled = True
            page.update()
        else:
            itunes_link.disabled = False
            page.update()

    def yt(d):
        if not youtube.value:
            youtube_link.disabled = True
            page.update()
        else:
            youtube_link.disabled = False
            page.update()

    def sc(d):
        if not soundcloud.value:
            soundcloud_link.disabled = True
            page.update()
        else:
            soundcloud_link.disabled = False
            page.update()

    page.add(Column([label, rtype, title, artist, img]))


    def submit(s):

        if rtype.value == "New Release":
            if beatport.value is True:
                btp = f"""
                <a href="{beatport_link.value}" target="_blank">
                    <button class = "beatport">
                        Beatport
                    </button>
                </a>
            """
            else:
                btp = ""

            if spotify.value:
                spt = f"""
                    <a target="_blank" href="{spotify_link.value}">
                        <button class = "spotify">
                            Spotify
                        </button>
                    </a>"""
            else:
                spt = ""

            if itunes.value:
                it = f"""
                    <a target="_blank"
                        href="{itunes_link.value}">
                            <button class = "itunes">
                                iTunes
                            </button>  
                    </a>
                """
            else:
                it = ""

            if youtube.value:
                yt = f"""
                <a target="_blank"
                    href="{youtube.value}">
                        <button class = "youtube">
                            You Tube
                        </button>       
                </a>
                """
            else:
                yt = ""

            if soundcloud.value:
                scl = f"""
                    <a target="_blank"
                        href="{soundcloud_link.value}">
                            <button class = "soundcloud">
                                Soundcloud
                            </button>   
                    </a>"""
            else:
                scl = ""
        else:

            if beatport.value:
                btp = f"""
                <a href="{beatport_link.value}" target="_blank">
                    <button class = "beatport">
                        Beatport
                    </button>
                </a>
            """
            else:
                btp = ""


            if spotify.value:
                spt = f"""
                    <a target="_blank" href="{spotify_link.value}">
                        <button class = "spotify">
                            Spotify
                        </button>
                    </a>"""
            else:
                spt = ""
            it = ""
            scl = ""
            yt = ""

        result = f'<body>\
        <link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@200&display=swap" rel="stylesheet">\
        <link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&display=swap" rel="stylesheet">\
        <div class = "head">\
        <div class = "head-cont">\
        <div class = "head-title">{label.value}</div>\
        <div class = "sub">{rtype.value}</div>\
        </div>\
        </div>\
        <div class = "release">\
        <img src="{img.value}">\
        </div>\
        <div class = "release-info">\
        <div class ="info">\
        <div class = "release-title">\
        {title.value}\
        </div>\
        <div class = "auth">\
        {artist.value}\
        </div>\
        </div>\
        </div>\
        <div class = "container">\
        <div class = "btn">\
        {btp}\
        {spt}\
        {it}\
        {yt}\
        {scl}\
        </div>\
        </div>\
        </body>'

        style = """<style>
        body {
        font-family: Julius Sans One, sans-serif;}
        .head {display: flex;
        margin: 0 auto;
        align-items: center;
        text-align: center;\
            padding: 10px;\
            margin-bottom: 20px;\
            }\
            .head-title {\
            font-size: larger;
            } 
            .head-cont {\
            display: flex;
            flex-direction: column;
            margin: 0 auto;
            }
            
            .sub {
            font-family: 'Source Code Pro', monospace;
            
            
            margin: 10px;
            font-size: 15px;
            font-weight:100;
            }
            
            .release {
            display: flex;
            
            margin: 0 auto;
            box-shadow: 0px 0px 5px 0px;
            display: flex;
            padding: 10px;
            border-radius: 10px;
            transition: 0.3s;
            width: 200px;
            height: 200px;
            }
            
            .release-info {
            display: flex;
            flex-direction: column;
            margin: 0 auto;
            }
            
            .release-title {
            font-weight: 900;
            font-size: large;
            
            }
            
            .auth {
            font-size: 15px;
            font-family: 'Source Code Pro', monospace;
            padding: 10px;
            
            }
            
            img {
            width: 200px;
            height: 200px;
            border-radius: 10px;
            }
            
            .info {
            text-align: center;
            padding: 15px;
            margin: 0 auto;
            }
            
            .beatport {
            color: rgb(1, 255, 149);
            }
            
            .beatport:hover {
            background-color:  rgb(1, 255, 149);
            color: white;
            transform: scale(110%);
            }
            
            .soundcloud {
            color: rgb(255,85,0)
            }
            
            .soundcloud:hover {
            
            background-color: rgb(255,85,0);
            color: white;
            transform: scale(110%);
            }
            
            .spotify {
            color: rgb(30 215 96)
            }
            
            .spotify:hover {
            
            background-color: rgb(30 215 96);
            color: white;
            transform: scale(110%);
            }
            
            .youtube {
            color: red;
            
            }
            
            .youtube:hover {
            
            background-color: red;
            color: white;
            transform: scale(110%);
            }
            
            .itunes{
            color: #fa57c1;
            }
            
            .itunes:hover {
            color: white;
            background-image: linear-gradient(to right, #fa57c1 0%, #b166cc 51%, #7572ff 100%);
            transform: scale(110%);
            }
            
            button {
            width:300px;
            font-family: Julius Sans One, sans-serif;
            font-weight: 900;
            height: 35px;
            margin: 3px;
            box-shadow: 0px 0px 2px 0px;
            background: none;
            border: solid 0.5px;
            border-radius: 10px;
            transition: 0.3s;
            }
            
            button:hover {
            box-shadow: 0px 0px 3px 0px;
            transition: 0.3s;
            }
            
            .btn {
            display: flex;
            flex-direction: column;
            align-items: center;
            }
            
            .container {
            
            width: 600px;
            height: 50px;
            
            /* Center horizontally*/
            margin: 0 auto;
            padding: 10px;
            width: fit-content;
            height: fit-content;
            }
            
            </style>"""


        pyperclip.copy(f"{result}{style}")

    beatport = Checkbox(on_change=lambda _: beat(_), value=True)
    beatport_link = TextField(label="Beatport Link", width=240)
    spotify = Checkbox(on_change=lambda _: spoty(_), value=True)
    spotify_link = TextField(label="Spotify Link", width=240)
    itunes = Checkbox(on_change=lambda _: itus(_), value=True)
    itunes_link = TextField(label="iTunes Link", width=240)
    youtube = Checkbox(on_change=lambda _: yt(_), value=True)
    youtube_link = TextField(label="Youtube Link", width=240)
    soundcloud = Checkbox(on_change=lambda _: sc(_), value=True)
    soundcloud_link = TextField(label="SoundCloud Link", width=240)

    content = Column([Row([beatport, beatport_link]), Row([spotify, spotify_link]), Row([itunes, itunes_link]),
                      Row([youtube, youtube_link]), Row([soundcloud, soundcloud_link])])

    page.add(content)

    copy_button = FilledButton("Submit", on_click=lambda _: submit(_))
    page.add(Row([copy_button], alignment=MainAxisAlignment.CENTER))


app(target=main)
