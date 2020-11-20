# Extracting_info_from_graphs
GUI to get data from a XY graph image, provided as a source path. 
The graph is considered rectangular and parallel to the edges of the picture.
Returned value is a list of tupples, holding the coordinates of the points in the graph.

During operation the user will be asked to fill:
 - Value of origin
 - A known value on X axis, to establish axis scale
 - A known value on Y axis, to establish axis scale

After that, the user will be asked to select the desired points on the graph imapge.

Selecting / deselecting process will be done by:
- Right-clicking or pressing 's' to select
- Left-clicking or pressing 'del' to deselect
- Middle-clicking or pressing 'Enter' to confirm
Note that while operating the keyboard may not work.
