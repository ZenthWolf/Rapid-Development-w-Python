
import sys
import wx

class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        self.b_test = wx.Button(self.panel, wx.ID_ANY, "Testing", pos=(60,20))
        self.Bind(wx.EVT_BUTTON, self.on_test, self.b_test)
        
        self.b_state = wx.Button(self.panel, wx.ID_ANY, "Disable", pos=(160,20))
        self.Bind(wx.EVT_BUTTON, self.on_state, self.b_state)

        self.cb_test = wx.ComboBox(self.panel, wx.ID_ANY, \
                                  choices=['Thor','Odin','Loki','Frigg','Freyr'], \
                                  pos=(270,20), style=wx.CB_SORT)
        self.cb_test.SetSelection(0)
        self.Bind(wx.EVT_COMBOBOX, self.on_select, self.cb_test)

        menubar = wx.MenuBar()
        menu_1 = wx.Menu()
        m_new = menu_1.Append(wx.ID_ANY, "New")
        m_open = menu_1.Append(wx.ID_ANY, "Open")
        m_recent = menu_1.Append(wx.ID_ANY, "Recent")
        m_quit = menu_1.Append(wx.ID_ANY, "Quit\tCTRL+Q")
        menubar.Append(menu_1, "File")

        menu_2 = wx.Menu()
        m_help = menu_2.Append(wx.ID_ANY, "Help\tF1")
        m_about = menu_2.Append(wx.ID_ANY, "About")
        menubar.Append(menu_2, "Help")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_new, m_new)
        self.Bind(wx.EVT_MENU, self.on_open, m_open)
        self.Bind(wx.EVT_MENU, self.on_recent, m_recent)
        self.Bind(wx.EVT_MENU, self.on_quit, m_quit)
        self.Bind(wx.EVT_MENU, self.on_help, m_help)
        self.Bind(wx.EVT_MENU, self.on_about, m_about)

    def on_new(self, event):
        print("New menu item")
        event.Skip()
    def on_open(self, event):
        print("Open menu item")
        event.Skip()
    def on_recent(self, event):
        print("Recent menu item")
        event.Skip()
    def on_quit(self, event):
        sys.exit(0)
    def on_help(self, event):
        print("Help menu item")
        event.Skip()
    def on_about(self, event):
        wx.MessageBox('wxPython Menu Demo', 'Info', wx.OK)
        event.Skip()
    
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
    
    def on_select(self, event):
        print(f"{self.cb_test.GetValue()} lives in Valhalla")

class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Test")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
