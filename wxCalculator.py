#Basic Calculator Challenge


import sys
import wx

class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        menubar = wx.MenuBar()
        menu_1 = wx.Menu()
        m_quit = menu_1.Append(wx.ID_ANY, "Quit\tCTRL+Q")
        menubar.Append(menu_1, "File")

        menu_2 = wx.Menu()
        m_about = menu_2.Append(wx.ID_ANY, "About")
        menubar.Append(menu_2, "Help")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_quit, m_quit)
        self.Bind(wx.EVT_MENU, self.on_about, m_about)
        
        self.rb_operation = wx.RadioBox(self.panel, label="Operation", choices=['+', '-', '*', '÷'], pos=(10,10))
        self.Bind(wx.EVT_RADIOBOX, self.on_select, self.rb_operation)
        
        self.tc_input0 = wx.TextCtrl(self.panel, value='Value', pos=(10,70), \
                                     size=(80,-1), style=wx.TEXT_ALIGNMENT_RIGHT)
        self.st_operator = wx.StaticText(self.panel,label='+', pos=(95,73), size=(-1,-1))
        self.tc_input1 = wx.TextCtrl(self.panel, value='Value', pos=(110,70), \
                                     size=(80,-1), style=wx.TEXT_ALIGNMENT_RIGHT)
        wx.StaticText(self.panel,label='=', pos=(195,73), size=(-1,-1))
        self.tc_output = wx.TextCtrl(self.panel, value='', pos=(210,70), \
                                     size=(80,-1), style=wx.TEXT_ALIGNMENT_RIGHT|wx.TE_READONLY)

        self.b_compute = wx.Button(self.panel, label="Compute", pos=(10,115))
        self.Bind(wx.EVT_BUTTON, self.on_compute, self.b_compute)

        self.operatedict={'+':self.on_add, '-':self.on_sub, \
                          '*':self.on_mult, '÷':self.on_div}
        
        self.lb_hist = wx.ListBox(self.panel,pos=(305,5), size=(150,200), \
                                  style=wx.LB_HSCROLL)

    
    def on_quit(self, event):
        sys.exit(0)
    def on_about(self, event):
        wx.MessageBox('wxPython Calculator Challenge.\nDoes simple arithmatic operations.', \
                       'Info', wx.OK)
        event.Skip()
    
    def on_select(self, event):
        self.st_operator.Label = self.rb_operation.GetString(self.rb_operation.GetSelection())

        event.Skip()
    
    def on_compute(self, event):
        try:
            a = float(self.tc_input0.Value)
        except ValueError:
            print("First Value is not a number")
            return
        try:
            b = float(self.tc_input1.Value)
        except ValueError:
            print("Second Value is not a number")
            return
        
        operator = self.rb_operation.GetString(self.rb_operation.GetSelection())
        output = str(self.operatedict[operator](a,b))
        self.tc_output.Value = output
        hist_entry=f'{str(a)} {operator} {str(b)} = {output}'
        self.lb_hist.InsertItems([hist_entry], 0)

        event.Skip()
    
    def on_add(self, a, b):
        return a+b
    def on_sub(self, a, b):
        return a-b
    def on_mult(self, a, b):
        return a*b
    def on_div(self, a, b):
        if b!=0:
            return a/b
        else:
            return 'NaN'

class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(None, wx.ID_ANY, title="wxPython Calculator Demo", size=(460,280))
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
