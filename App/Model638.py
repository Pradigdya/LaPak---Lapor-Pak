import DBConnection


def getLaporan(limit=5, offset=0):

    conn = DBConnection.get_db_connection()

    laporan1 = conn.execute("SELECT * FROM laporan638 ORDER BY id_laporan ASC LIMIT ? OFFSET ?", (limit, offset)).fetchall()

    conn.close()

    return laporan1


def getTotalLaporan():

    conn = DBConnection.get_db_connection()

    total = conn.execute("SELECT COUNT(*) AS total FROM laporan638").fetchone()["total"]

    conn.close()

    return total


def getLaporanById(id_laporan):

    conn = DBConnection.get_db_connection()

    laporan = conn.execute("SELECT * FROM laporan638 WHERE id_laporan = ?", (id_laporan,)).fetchone()

    conn.close()

    return laporan


def tambahLaporan(nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan):

    conn = DBConnection.get_db_connection()

    conn.execute("INSERT INTO laporan638 (nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan) VALUES (?, ?, ?, ?, ?)", 
                 (nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan))

    conn.commit()

    conn.close()

    return True


def updateLaporan(id_laporan, nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan):

    conn = DBConnection.get_db_connection()

    conn.execute("UPDATE laporan638 SET nama_pelapor = ?, jenis_sampah = ?, lokasi_masalah = ?, tanggal_kejadian = ?, prioritas_penanganan = ? WHERE id_laporan = ?", 
                 (nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan, id_laporan))

    conn.commit()

    conn.close()

    return True


def hapusLaporan(id_laporan):

    conn = DBConnection.get_db_connection()

    conn.execute("DELETE FROM laporan638 WHERE id_laporan = ?", (id_laporan,))

    conn.commit()

    conn.close()

    return True







