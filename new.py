import folium
import osmnx as ox
import networkx as nx

# Tọa độ của các điểm cần tìm đường (ví dụ A và B)
point_a = (21.000338866478234, 105.84245825765474)  # Điểm A
point_b = (21.00543631047863, 105.8455027703646)  # Điểm B

# Tải đồ thị giao thông trong bán kính 1km xung quanh điểm A để bao trùm cả điểm B
graph = ox.graph_from_point(point_a, dist=1000, network_type='drive')

# Tìm các nút gần nhất với tọa độ của A và B
node_a = ox.nearest_nodes(graph, point_a[1], point_a[0])  # Chú ý thứ tự long, lat
node_b = ox.nearest_nodes(graph, point_b[1], point_b[0])

# Tìm đường ngắn nhất từ A đến B dựa trên chiều dài đường đi thực tế
shortest_path = nx.shortest_path(graph, source=node_a, target=node_b, weight='length')

# Tạo bản đồ Folium
m = folium.Map(location=point_a, zoom_start=15)

# Lấy danh sách tọa độ của đường đi ngắn nhất
route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in shortest_path]

# Vẽ đường đi trên bản đồ
folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)

# Đánh dấu điểm A và điểm B
folium.Marker(location=point_a, popup="Điểm A", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(location=point_b, popup="Điểm B", icon=folium.Icon(color="red")).add_to(m)

# Lưu và mở bản đồ
m.save("shortest_route_map.html")
print("Đã tạo bản đồ với đường đi ngắn nhất giữa A và B!")
