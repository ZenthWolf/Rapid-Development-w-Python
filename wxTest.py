import wx

class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        wx.StaticText(self.panel, wx.ID_ANY, "Some static text", pos=(5,60))
        
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,20))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        
        self.b_state = wx.Button(self.panel, wx.ID_ANY, "Disable", pos=(160,20))
        self.Bind(wx.EVT_BUTTON, self.on_state, self.b_state)

        #Check Box Example
#        self.cb_discount = wx.CheckBox(self.panel, wx.ID_ANY, "Apply Discount", \
#                                       pos = (5, 100))
        #Radio buttons as single declaration
        self.rb_planet = wx.RadioBox(self.panel, wx.ID_ANY, label="Planets", \
                                     pos = (60, 100), choices=['Venus', 'Earth', 'Mars'])
        #Radio buttons as separate declarions
        #Even the demonstration didn't work on this one
#        self.rb_venus = wx.RadioButton(self.panel, wx.ID_ANY, label="Venus",\
#                                       pos=(66,100), style=wx.RB_SINGLE)
#        self.rb_earth = wx.RadioButton(self.panel, wx.ID_ANY, label="Earth",\
#                                       pos=(133,100), style=wx.RB_SINGLE)
#        self.rb_mars = wx.RadioButton(self.panel, wx.ID_ANY, label="Mars",\
#                                       pos=(199,100), style=wx.RB_SINGLE)
    
    def on_test(self, event):
        #On Press, print set message
#        print("Button pressed")

        #On Press, print message from check box
#        print(f"Checkbox {self.cb_discount.IsChecked()}")
        #On Press, print message from radio box selection
        print(self.rb_planet.GetStringSelection())
        #On Press, print message from single radio buttons
#        if self.rb_venus.GetValue(): print("Venutian Skies")
#        if self.rb_earth.GetValue(): print("Welcome to Earth")
#        if self.rb_mars.GetValue():  print("Martian Dream")

        event.Skip()
    
    def on_state(self, event):
        if self.b_state.GetLabel()=="Disable":
            self.b_test.Disable()
            self.b_state.SetLabel("Enable")
        
        else:
            self.b_test.Enable()
            self.b_state.SetLabel("Disable")
        
        event.Skip()


class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
