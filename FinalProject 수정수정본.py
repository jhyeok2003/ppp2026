import os
import sqlite3
import random
import json
import matplotlib.pyplot as plt
import PySimpleGUI as sg

plt.rc("font", family="Times New Roman")
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def create_table():
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS songs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        singer TEXT,
        genre TEXT,
        likes INTEGER
    )
    """

    cur.execute(sql_query)
    conn.commit()
    conn.close()


def insert_song(title, singer, genre):
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    INSERT INTO songs (title, singer, genre, likes) 
    VALUES (?, ?, ?, ?)
    """

    data_tuple = (title, singer, genre, 0)
    cur.execute(sql_query, data_tuple)

    conn.commit()
    conn.close()


def load_song():
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    SELECT id, title, singer, genre, likes 
    FROM songs
    """

    cur.execute(sql_query)
    songs_data = cur.fetchall()

    conn.close()
    return songs_data


def delete_song(song_id):
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    DELETE FROM songs 
    WHERE id = ?
    """

    data_tuple = (song_id,)
    cur.execute(sql_query, data_tuple)

    conn.commit()
    conn.close()


def like_song(song_id):
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    UPDATE songs 
    SET likes = likes + 1 
    WHERE id = ?
    """

    data_tuple = (song_id,)
    cur.execute(sql_query, data_tuple)

    conn.commit()
    conn.close()


def search_song(keyword):
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    SELECT id, title, singer, genre, likes 
    FROM songs 
    WHERE title LIKE ?
    """

    search_word = f"%{keyword}%"
    data_tuple = (search_word,)
    cur.execute(sql_query, data_tuple)

    songs_data = cur.fetchall()
    conn.close()

    return songs_data


def get_random_song():
    songs_list = load_song()
    songs_count = len(songs_list)

    if songs_count == 0:
        return None

    random_picked_song = random.choice(songs_list)
    return random_picked_song


def recommend_genre():
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    SELECT genre, COUNT(*) 
    FROM songs 
    GROUP BY genre 
    ORDER BY COUNT(*) DESC
    """

    cur.execute(sql_query)
    recommended_data = cur.fetchall()
    conn.close()

    data_length = len(recommended_data)
    if data_length == 0:
        return "없음"

    result_genre_name = recommended_data[0][0]
    return result_genre_name


def save_json():
    songs_list = load_song()
    json_backup_list = []

    for song_item in songs_list:
        song_dict = {
            "id": song_item[0],
            "title": song_item[1],
            "singer": song_item[2],
            "genre": song_item[3],
            "likes": song_item[4]
        }
        json_backup_list.append(song_dict)

    try:
        with open("playlist.json", "w", encoding="utf-8") as json_file:
            json.dump(json_backup_list, json_file, ensure_ascii=False, indent=4)
    except:
        pass


def load_json():
    try:
        with open("playlist.json", "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        conn = sqlite3.connect("music.db")
        cur = conn.cursor()

        delete_query = "DELETE FROM songs"
        cur.execute(delete_query)

        for song_item in json_data:
            insert_query = """
            INSERT INTO songs (title, singer, genre, likes) 
            VALUES (?, ?, ?, ?)
            """

            data_tuple = (
                song_item["title"],
                song_item["singer"],
                song_item["genre"],
                song_item["likes"]
            )
            cur.execute(insert_query, data_tuple)

        conn.commit()
        conn.close()
    except:
        pass


def show_graph():
    conn = sqlite3.connect("music.db")
    cur = conn.cursor()

    sql_query = """
    SELECT genre, COUNT(*) 
    FROM songs 
    GROUP BY genre
    """

    cur.execute(sql_query)
    graph_data = cur.fetchall()
    conn.close()

    genre_names = []
    genre_counts = []

    for row in graph_data:
        name_val = row[0]
        count_val = row[1]
        genre_names.append(name_val)
        genre_counts.append(count_val)

    total_names_count = len(genre_names)
    if total_names_count == 0:
        return

    plt.bar(genre_names, genre_counts)
    plt.title("Genre Statistics")
    plt.show()


def update_list(window):
    songs_list = load_song()
    formatted_list = []

    for song_item in songs_list:
        id_val = song_item[0]
        title_val = song_item[1]
        singer_val = song_item[2]
        genre_val = song_item[3]
        likes_val = song_item[4]

        list_text = f"{id_val} | {title_val} | {singer_val} | {genre_val} | ❤️{likes_val}"
        formatted_list.append(list_text)

    window["LIST"].update(formatted_list)


def make_window():
    title_text = sg.Text("Music Mate", font=("Arial", 20))

    label_title = sg.Text("제목")
    input_title = sg.Input(key="TITLE")

    label_singer = sg.Text("가수")
    input_singer = sg.Input(key="SINGER")

    label_genre = sg.Text("장르")
    combo_genre = sg.Combo(["발라드", "KPOP", "힙합", "POP"], default_value="발라드", key="GENRE")

    btn_add = sg.Button("추가")
    btn_del = sg.Button("삭제")

    separator_line = sg.HorizontalSeparator()

    label_search = sg.Text("노래 검색")
    input_search = sg.Input(key="SEARCH")
    btn_search = sg.Button("검색")

    listbox_output = sg.Listbox(values=[], size=(60, 12), key="LIST")

    btn_like = sg.Button("좋아요")
    btn_random = sg.Button("랜덤추천")

    btn_genre_rec = sg.Button("장르추천")
    btn_graph = sg.Button("그래프")

    btn_json_save = sg.Button("JSON저장")
    btn_json_load = sg.Button("JSON불러오기")

    message_text = sg.Text("", key="MESSAGE", size=(60, 1), text_color="blue", font=("Arial", 11))

    window_layout = [
        [title_text],
        [label_title],
        [input_title],
        [label_singer],
        [input_singer],
        [label_genre],
        [combo_genre],
        [btn_add, btn_del],
        [separator_line],
        [label_search],
        [input_search],
        [btn_search],
        [listbox_output],
        [btn_like, btn_random],
        [btn_genre_rec, btn_graph],
        [btn_json_save, btn_json_load],
        [message_text]
    ]

    my_application_window = sg.Window("Music Mate", window_layout, size=(600, 670), finalize=True)
    return my_application_window


def main():
    create_table()
    main_window = make_window()
    update_list(main_window)

    while True:
        event, values = main_window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "추가":
            title_value = values["TITLE"]
            singer_value = values["SINGER"]
            genre_value = values["GENRE"]

            if title_value == "" or singer_value == "":
                main_window["MESSAGE"].update("제목과 가수를 입력하세요.")
            else:
                insert_song(title_value, singer_value, genre_value)
                update_list(main_window)
                main_window["MESSAGE"].update("노래가 추가되었습니다.")

        elif event == "삭제":
            try:
                selected_item = values["LIST"][0]
                song_id = int(selected_item.split("|")[0].strip())
                delete_song(song_id)
                update_list(main_window)
                main_window["MESSAGE"].update("삭제 완료")
            except:
                main_window["MESSAGE"].update("삭제할 노래를 선택하세요.")

        elif event == "좋아요":
            try:
                selected_item = values["LIST"][0]
                song_id = int(selected_item.split("|")[0].strip())
                like_song(song_id)
                update_list(main_window)
                main_window["MESSAGE"].update("좋아요 +1")
            except:
                main_window["MESSAGE"].update("노래를 선택하세요.")

        elif event == "검색":
            search_keyword = values["SEARCH"]
            search_result_data = search_song(search_keyword)
            search_display_list = []

            for song_item in search_result_data:
                res_id = song_item[0]
                res_title = song_item[1]
                res_singer = song_item[2]
                res_genre = song_item[3]
                res_likes = song_item[4]

                search_text = f"{res_id} | {res_title} | {res_singer} | {res_genre} | ❤️{res_likes}"
                search_display_list.append(search_text)

            main_window["LIST"].update(search_display_list)

        elif event == "랜덤추천":
            recommended_song = get_random_song()

            if recommended_song is None:
                main_window["MESSAGE"].update("저장된 노래가 없습니다.")
            else:
                rec_title = recommended_song[1]
                rec_singer = recommended_song[2]
                recommend_text = f"추천곡 : {rec_title} - {rec_singer}"
                main_window["MESSAGE"].update(recommend_text)

        elif event == "장르추천":
            recommended_genre = recommend_genre()
            main_window["MESSAGE"].update(f"추천 장르 : {recommended_genre}")

        elif event == "그래프":
            show_graph()

        elif event == "JSON저장":
            save_json()
            main_window["MESSAGE"].update("JSON 저장 완료")

        elif event == "JSON불러오기":
            load_json()
            update_list(main_window)
            main_window["MESSAGE"].update("JSON 불러오기 완료")

    main_window.close()


if __name__ == '__main__':
    main()