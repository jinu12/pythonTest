import wx
import weather
import itemdb

app = wx.App()
frame = wx.Frame(None, 0, 'Test')

p1 = wx.Panel(frame)
bt1 = wx.Button(p1, label='Button1')
bt2 = wx.Button(p1, label='Button2')
bt3 = wx.Button(p1, label='Button3')
ps = wx.BoxSizer(wx.VERTICAL)
ps.Add(bt1)
ps.Add(bt2)
ps.Add(bt3)
p1.SetSizer(ps)

p2 = wx.Panel(frame)
names = ['abc', 'eds', 'fse', 'gfsd']
lists = wx.ListBox(p2, choices=names)
lists.SetSize(wx.Size(300, 200))

p3 = wx.Panel(frame)
bt_add = wx.Button(p3, label='ADD')
text1 = wx.TextCtrl(p3)
text2 = wx.TextCtrl(p3)
text3 = wx.TextCtrl(p3)
text4 = wx.TextCtrl(p3)
ps3 = wx.BoxSizer(wx.VERTICAL)
ps3.Add(bt_add)
ps3.Add(text1)
ps3.Add(text2)
ps3.Add(text3)
ps3.Add(text4)
p3.SetSizer(ps3)


box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(p1, border=10, flag=wx.DOWN)
box.Add(p2, border=10, flag=wx.UP)
box.Add(p3, border=10, flag=wx.UP)


def clickbt1(click):
    lists.Clear()
    items = weather.getdata()
    lists.AppendItems(items)


def clickbt2(click):
    lists.Clear()
    items = itemdb.select_ui()
    lists.AppendItems(items)


def clickbt3(click):
    lists.Clear()
    items = ['555', '666', '777', '888']
    lists.AppendItems(items)


def clickadd(click):
    id = int(text1.GetValue())
    name = text2.GetValue()
    price = int(text3.GetValue())
    rate = float(text4.GetValue())
    try:
        itemdb.insert(id, name, price, rate)
        text1.SetLabelText('')
        text2.SetLabelText('')
        text3.SetLabelText('')
        text4.SetLabelText('')
    except:
        wx.MessageBox('Insert Error', 'Alert', wx.OK)
        raise


bt_add.Bind(wx.EVT_BUTTON, clickadd)


bt1.Bind(wx.EVT_BUTTON, clickbt1)
bt2.Bind(wx.EVT_BUTTON, clickbt2)
bt3.Bind(wx.EVT_BUTTON, clickbt3)


frame.Show(True)
app.MainLoop()
