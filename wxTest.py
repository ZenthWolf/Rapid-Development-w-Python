
import wx

class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,20))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        
        self.b_state = wx.Button(self.panel, wx.ID_ANY, "Disable", pos=(160,20))
        self.Bind(wx.EVT_BUTTON, self.on_state, self.b_state)
        self.tc_ctr = wx.TextCtrl(self.panel, wx.ID_ANY, "1", (60,100), (35,-1))
        hispin = self.tc_ctr.GetSize().height
        pospin = self.tc_ctr.GetSize().width + self.tc_ctr.GetPosition().x + 2
        #Definitely not confusing given that SpinCtrl is also a wx class.
        self.sb_ctr = wx.SpinButton(self.panel, wx.ID_ANY, (pospin,100), \
                                    (int(hispin*3/4),hispin), style=wx.SP_VERTICAL | wx.SP_ARROW_KEYS)
        self.sb_ctr.SetRange(1,100)
        self.sb_ctr.SetValue(1)
        self.Bind(wx.EVT_SPIN, self.on_spin, self.sb_ctr)
    
    def on_test(self, event):
        #On Press, print set message
        print("This button works.")
        event.Skip()
    
    def on_state(self, event):
        if self.b_state.GetLabel()=="Disable":
            self.b_test.Disable()
            self.b_state.SetLabel("Enable")
        
        else:
            self.b_test.Enable()
            self.b_state.SetLabel("Disable")
        
        event.Skip()
    
    def on_spin(self, event):
        self.tc_ctr.SetValue(str(event.GetPosition()))
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
