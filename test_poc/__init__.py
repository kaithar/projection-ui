import projection
from projection import elements


class Viewer(projection.Viewer):
  def __init__(self, application, websocket):
    super(Viewer, self).__init__(application, websocket)
    print("Viewer")
    self.title = "Test thing"
    con = elements.div.Container(column = 3, row = 2, width = 2)
    con.border = '1px solid grey'
    div = elements.div.Div("Test div")
    div.content = "Foooo"
    con.append(div)
    self.append(con)
