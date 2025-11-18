import DBConnection


def getLaporan(limit=5, offset=0):

    conn = DBConnection.get_db_connection()

    laporan1 = conn.execute("SELECT * FROM laporan631 ORDER BY id_laporan ASC LIMIT ? OFFSET ?", (limit, offset)).fetchall()

    conn.close()

    return laporan1


def getTotalLaporan():

    conn = DBConnection.get_db_connection()

    total = conn.execute("SELECT COUNT(*) AS total FROM laporan631").fetchone()["total"]

    conn.close()

    return total


def getLaporanById(id_laporan):

    conn = DBConnection.get_db_connection()

    laporan = conn.execute("SELECT * FROM laporan631 WHERE id_laporan = ?", (id_laporan,)).fetchone()

    conn.close()

    return laporan


def tambahLaporan(nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan):

    conn = DBConnection.get_db_connection()

    conn.execute("INSERT INTO laporan631 (nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan) VALUES (?, ?, ?, ?, ?)", 
                 (nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan))

    conn.commit()

    conn.close()

    return True


def updateLaporan(id_laporan, nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan):

    conn = DBConnection.get_db_connection()

    conn.execute("UPDATE laporan631 SET nama_pelapor = ?, rt = ?, lokasi_jalan = ?, tingkat_kerusakan = ?, deskripsi_kerusakan = ? WHERE id_laporan = ?", 
                 (nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan, id_laporan))

    conn.commit()

    conn.close()

    return True


def hapusLaporan(id_laporan):

    conn = DBConnection.get_db_connection()

    conn.execute("DELETE FROM laporan631 WHERE id_laporan = ?", (id_laporan,))

    conn.commit()

    conn.close()

    return True