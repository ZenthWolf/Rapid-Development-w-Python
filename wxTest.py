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
    
    def on_test(self, event):
        print("Button pressed")
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
