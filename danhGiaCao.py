import requests

# URL của endpoint để lấy danh sách phim được đánh giá cao nhất
url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

# Header chứa mã token của bạn
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NzM5ZWJiN2Q2NmZhMWRkNzc1ZjgwNjMyNWFiNDA2NyIsIm5iZiI6MTczMjU0MjQ5MS43MzgsInN1YiI6IjY3NDQ4MDFiYzI0NzY1ZmEyZjJkZThjYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QxVbmCFgGwJ_uP1JOUdhZWrGbPBPMRpeI4OAdtl2EFs"
}

# Gửi yêu cầu GET đến API
response = requests.get(url, headers=headers)

# Kiểm tra mã trạng thái HTTP (200 là thành công)
if response.status_code == 200:
    data = response.json()  # Chuyển phản hồi JSON thành đối tượng Python
    # Duyệt qua danh sách các bộ phim trong phần 'results'
    for idx, movie in enumerate(data['results'], start=1):
        title = movie['title']
        release_date = movie.get('release_date', 'N/A')  # Nếu không có ngày phát hành, hiển thị 'N/A'
        vote_average = movie['vote_average']
        print(f"{idx}. {title} (Release Date: {release_date}, Rating: {vote_average})")
else:
    print(f"Error: {response.status_code}, {response.text}")
