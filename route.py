from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from user import User
from myrecording import Myrecording
from artist import Artist
from jeu import Jeu
from mystatus import Mystatus
from photo import Photo
from tweet import Tweet
from myemail import Email


from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("premiere radio")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbScript=Myscript()
        self.dbRecording=Myrecording()
        self.dbMystatus=Mystatus()
        self.dbEmail=Email()
        self.dbPhoto=Photo()
        self.dbTweet=Tweet()
        self.dbJeu=Jeu()
        self.dbArtist=Artist()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
          print("set session",x)
          hey={}
          for a in x:
              hey[a]=params[a][0]
          return hey
          
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def chat(self,search):
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/chat.html")
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def audio_save(self,search):
        myparam=self.get_post_data()(params=("recording",))
        hi=self.dbRecording.create(myparam)
        return self.render_some_json("welcome/hey.json")
    def allscript(self,search):
        #myparam=self.get_post_data()(params=("name","content",))
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/allscript.html")
    def lancerscript(self,search):
        myparam=search["myid"][0]
        hi=self.dbScript.getbyid(myparam)
        print(hi, "my script")
        a=self.scriptpython(hi["name"]).lancer()
        return self.render_some_json("welcome/monscript.json")

    def cartedidentite(self,search):
        self.Program.set_nocache(True)
        print("carte user")
        print("user  ",self.Program.get_session())
        userid=self.Program.get_session_param("user_id")
        print("user id ",userid)

        if userid != "":
          self.render_figure.set_param("user",self.dbUsers.getbyid(userid))
          return self.render_figure.render_figure("user/carte.html")
        else:
          self.set_redirect("/youbank")
          self.set_my_session({"notice":"vous n'êtes pas connecté à la banque"})
          return self.render_figure.render_redirect()

    def check_mailbox(self,search):
        hi=self.dbEmail.createfake()
        hi1=self.dbEmail.createfake()
        hi2=self.dbEmail.createfake()
        hi4=self.dbEmail.createfake()
        self.render_figure.set_param("emails",(hi,hi1,hi2,hi4))
        return self.render_some_json("email/emails.json")
    def tweeter(self,search):
        myparam=self.get_post_data()(params=("user_id","text",))
        hi=self.dbTweet.create(myparam)
        self.render_figure.set_param("redirect","/tweet_details")
        return self.render_some_json("welcome/redirect.json")
    def addphoto(self,search):
        myparam=self.get_post_data()(params=("user_id","pic",))
        hi=self.dbPhoto.create(myparam)
        self.render_figure.set_param("redirect","/post_hom_office")
        return self.render_some_json("welcome/redirect.json")
    def mystatus(self,search):
        myparam=self.get_post_data()(params=("text",))
        hi=self.dbMystatus.create(myparam)
        self.render_figure.set_param("redirect","/post_hom_office")
        return self.render_some_json("welcome/redirect.json")
    def new1(self,search):
        myparam=self.get_post_data()(params=("script","missiontarget_id","missiontype_id","missionprogram_id",))
        #hi=self.dbMissionscript.create(myparam)
        return self.render_some_json("welcome/mypic.json")
    def monscript(self,search):
        myparam=self.get_post_data()(params=("name","content",))
        hey=self.dbCommandline.create(myparam)
        hi=self.dbScript.create(myparam)
        print(hey,hi)
        return self.render_some_json("welcome/monscript.json")
    def enregistrer(self,search):
        print("hello action")
        self.render_figure.set_param("enregistrer",True)
        return self.render_figure.render_figure("welcome/radio.html")
    def hello(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/index.html")
    def tweet_details(self,search):
        print("hello action")
        self.render_figure.set_param("tweets",self.dbTweet.getall())
        return self.render_figure.render_figure("twitter/tweet.html")
    def fill_in_inbox(self,search):
        print("hello action")
        self.render_figure.set_param("emails",self.dbEmail.getall())
        return self.render_figure.render_figure("email/email.html")
    def post_hom_office(self,search):
        print("hello action")
        self.render_figure.set_param("shared",self.dbMystatus.getall())
        self.render_figure.set_param("photos",self.dbPhoto.getall())
        return self.render_figure.render_figure("facebook/page.html")
    def youbank_inscription(self,search):
        print("hello action")
        return self.render_figure.render_figure("bank/signup.html")
    def youbank(self,search):
        print("hello action")
        return self.render_figure.render_figure("bank/youbank.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def voiremail(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("email",self.dbEmail.getbyid(myparam["id"]))
        return self.render_figure.render_only_figure("email/voiremail.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        return self.render_figure.set_param("user",User().getbyid(myparam["id"]))
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("user/users.html")
    def mypics(self,params={}):
        self.render_figure.set_param("pics",self.dbFish.getall())
        return self.render_figure.render_figure("fish/fishes.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password","password_security"))
        self.user=self.dbUsers.getbyemailpwsecurity(search["email"],search["password"],search["password_security"])
        print("user trouve", self.user)
        if self.user["email"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/cartedidentite\"}")
        else:
            self.set_json("{\"redirect\":\"/youbank\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")
    def getlyrics(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("lyrics",hey)
        return self.render_some_json("welcome/lyrics.json")
    def photoartist(self,params={}):
        myparam=self.get_post_data()(params=("pic","id",))
        hey=self.dbArtist.update(myparam)
        return self.render_some_json("welcome/create.json")
    def jouerjeux(self,search):
        return self.render_figure.render_figure("welcome/jeu.html")
    def monjeu(self,search):
        myparam=self.get_post_data()(params=("lyric_id",))

        hi=self.dbJeu.createwithlyric(myparam)
        print(hi)
        self.render_figure.set_param("redirect","/jouerjeux")
        return self.render_some_json("welcome/redirect.json")

    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("email","password","password_security","nomcomplet"))
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/youbank\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/youbank_inscription\"}")
            return self.render_figure.render_json()
    def joueraujeu(self,params={}):
        self.set_json("{\"redirect\":\"/signin\"}")
        getparams=("song_id","jeu_id")
        myparam=self.get_post_data()(params=getparams)
        self.set_session_params(myparam)
        #self.set_redirect("/signin")
        #return self.render_figure.render_redirect()
        return self.render_figure.render_my_json("{\"redirect\":\"/signin\"}")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
                    '^/cartedidentite': self.cartedidentite,
                    '^/check_mailbox': self.check_mailbox,
                    '^/tweeter$': self.tweeter,
                    '^/tweet_details$': self.tweet_details,
                    '^/addphoto$': self.addphoto,
                    '^/mystatus$': self.mystatus,
                    '^/fill_in_inbox$': self.fill_in_inbox,
                    '^/post_hom_office$': self.post_hom_office,
                    '^/youbank$': self.youbank,
                    '^/youbank_inscription$': self.youbank_inscription,
                    '^/new$': self.nouveau,
                    '^/welcome$': self.welcome,
                    '^/signin$': self.signin,
                    '^/logmeout$':self.logout,
                                        '^/save_user$':self.save_user,
                                                            '^/update_user$':self.update_user,
                    "^/voiremail/([0-9]+)$":self.voiremail,
                    "^/seeuser/([0-9]+)$":self.seeuser,
                                        "^/edituser/([0-9]+)$":self.edit_user,
                                                            "^/deleteuser/([0-9]+)$":self.delete_user,
                                                                                '^/login$':self.login,

                                                                                                    '^/users$':self.myusers,
                    '^/$': self.hello

                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       self.Program.set_html(html=mycase(params))
                   except Exception:  
                       self.Program.set_html(html="<p>une erreur s'est produite "+str(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>")
                   #self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
