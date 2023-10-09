
// 座標とズームレベルを指定 例：東京
const map = L.map('map').setView([35.681167, 139.767052], 10);
print("gの値は",g)

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    // 右下にクレジットを表示
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// マーカーの追加 例：東京駅
var marker = L.marker([35.681167, 139.767052]).addTo(map);

// 円の追加 例：東京駅
var circle = L.circle([35.681167, 139.767052], {
    color: 'blue',
    fillColor: '#4169e1',
    fillOpacity: 0.4,
    radius: 1000
  }).addTo(map);

marker.bindPopup(g+h+"<b>東京駅</b><br>東京都千代田区丸の内一丁目にある、東日本旅客鉄道・東海旅客鉄道・東京地下鉄の駅")
// 画面表示時にポップアップする
.openPopup();
  

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("クリック位置 " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);