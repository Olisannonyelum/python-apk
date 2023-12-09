import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase,MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel




class root(MDBoxLayout):
    def __init__(self,**kwarge):
        super().__init__(**kwarge)
        self.orientation='vertical'
        self.add_widget(MDTopAppBar())
        self.Tabs_pannel=MDTabs()
        self.add_widget(self.Tabs_pannel)

#class content()

class Tab_items(MDBoxLayout,MDTabsBase):
    def __init__(self,**kwarge):
        super().__init__(**kwarge)
        self.orientation='vertical'
        self.content=MDLabel(halign="center",text="hello")

#class Tab(MDBoxLayout, MDTabsBase):
 #   pass
        

class my_app(MDApp):
    def build (self):
        self.body=root()

        #self.tab_pannel=root().Tabs_pannel
        self.body.Tabs_pannel.add_widget(Tab_items(title="tab 1"))
        self.body.Tabs_pannel.add_widget(Tab_items(title="tab 2"))
        
        #self.tab_pannel.add_widget(Tab_items(title="tab 2"))
        
        #self.body.add_widget(self.tab_pannel)

#        self.body=root()
 #       self.tap=self.body.Tabs_#.ids.Tabs
  #      tab_item_1=Tab_items(title="tab 1")
   #     tab_item_2=Tab_items(title="tab 2")
    #    self.tap.add_widget(tab_item_1)
     #   self.tap.add_widget(tab_item_2)
      #  self.body.add_widget(self.tap)
        


        return self.body
        #return Builder.load_string(KV)

if __name__=='__main__':
    my_app().run()
