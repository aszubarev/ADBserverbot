def insert_record(db, name, year):

    cur = db.cursor()
    cur.execute('INSERT IGNORE INTO main (`Название публикации`, `Год издания`) VALUES (%s, %s)', (name, year))
    db.commit()


# select all publications
def select_pb(db):

    cur = db.cursor()
    cur.execute('SELECT `Название публикации` FROM main')
    db.commit()

    answer = list()
    for str_name in cur:
        answer.append(str_name[0])

    return answer
