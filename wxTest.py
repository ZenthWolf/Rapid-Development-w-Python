
import wx

class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,20))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        
        self.b_state = wx.Button(self.panel, wx.ID_ANY, "Disable", pos=(160,20))
        self.Bind(wx.EVT_BUTTON, self.on_state, self.b_state)

        self.lb_test = wx.ListBox(self.panel, wx.ID_ANY, \
                                  choices=['Thor','Odin','Loki','Frigg','Freyr'], \
                                  style=wx.LB_HSCROLL | wx.LB_SINGLE | wx.LB_SORT, \
                                  pos=(270,20), size=(120,160))
        self.lb_test.SetSelection(0)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_click, self.lb_test)
        self.tc_test = wx.TextCtrl(self.panel,wx.ID_ANY, "", pos=(60,70))
    
    def on_test(self, event):
        #On Press, print set message
        #print("This button works.")
        
        #Prints highlight entry
        #listno = self.lb_test.GetSelection()
        #print(f"{self.lb_test.GetString(listno)} lives in Valhalla")
        
        #Adds an entry
        self.lb_test.Append(self.tc_test.GetValue())
        
        #Removes selected entry
        listno = self.lb_test.GetSelection()
        print(self.lb_test.Count)
        self.lb_test.Delete(listno)
        print(self.lb_test.Count)
        event.Skip()
    
    def on_state(self, event):
        if self.b_state.GetLabel()=="Disable":
            self.b_test.Disable()
            self.b_state.SetLabel("Enable")
        
        else:
            self.b_test.Enable()
            self.b_state.SetLabel("Disable")
        
        event.Skip()
    
    def on_click(self, event):
        listno = self.lb_test.GetSelection()
        print(f"{self.lb_test.GetString(listno)} lives in Valhalla")

class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
