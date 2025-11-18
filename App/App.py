from flask import Flask, render_template, request, redirect, url_for, jsonify, flash

import math

import DBConnection
import Model631
import Model638



app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  

@app.route('/')

def home():

    
    return render_template('profile.html')




@app.route('/laporan')
def laporan():
    return render_template('laporan.html')

@app.route('/laporan/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        
        data = request.get_json(force=True)
        
        nama_pelapor = data.get('namaPelapor631')
        rt = data.get('rtRw631')
        lokasi_jalan = data.get('lokasiJalan631')
        tingkat_kerusakan = data.get('tingkatKerusakan631')
        deskripsi_kerusakan = data.get('deskripsiKerusakan631')
        
        try:
            Model631.tambahLaporan(nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan)
            flash('✅ Data berhasil ditambahkan.', 'success')
            return jsonify({'success': True, 'redirect': url_for('laporantabel')}), 200
        except Exception as e:
            flash(f'❌ Gagal menambahkan data: {e}', 'danger')
            return jsonify({'success': False, 'error': str(e)}), 500
    
    return render_template('laporan1.html', action='Tambah', laporan=None)

@app.route('/laporan/edit/<int:id>', methods=['GET', 'PUT'])
def edit(id):
    if request.method == 'PUT':
        
        data = request.get_json(force=True)
        
        nama_pelapor = data.get('namaPelapor631')
        rt = data.get('rtRw631')
        lokasi_jalan = data.get('lokasiJalan631')
        tingkat_kerusakan = data.get('tingkatKerusakan631')
        deskripsi_kerusakan = data.get('deskripsiKerusakan631')
        
        try:
            Model631.updateLaporan(id, nama_pelapor, rt, lokasi_jalan, tingkat_kerusakan, deskripsi_kerusakan)
            flash('✅ Data berhasil diperbarui.', 'success')
            return jsonify({'success': True, 'redirect': url_for('laporantabel')}), 200
        except Exception as e:
            flash(f'❌ Gagal memperbarui data: {e}', 'danger')
            return jsonify({'success': False, 'error': str(e)}), 500
    
    laporan = Model631.getLaporanById(id)
    return render_template('laporan1.html', action='Edit', laporan=laporan)

@app.route('/laporan/1')
def laporan1():
    return redirect(url_for('tambah'))


@app.route('/laporan/tambah2', methods=['GET', 'POST'])
def tambah2():
    if request.method == 'POST':
        
        data = request.get_json(force=True)
        
        nama_pelapor = data.get('namaPelapor638')
        jenis_sampah = data.get('jenisMasalah638')
        lokasi_masalah = data.get('lokasiPermasalahan638')
        tanggal_kejadian = data.get('tanggalKejadian638')
        prioritas_penanganan = data.get('prioritas638')
        
        try:
            Model638.tambahLaporan(nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan)
            flash('✅ Data berhasil ditambahkan.', 'success')
            return jsonify({'success': True, 'redirect': url_for('laporantabel')}), 200
        except Exception as e:
            flash(f'❌ Gagal menambahkan data: {e}', 'danger')
            return jsonify({'success': False, 'error': str(e)}), 500
    
    return render_template('laporan2.html', action='Tambah', laporan=None)

@app.route('/laporan/edit2/<int:id>', methods=['GET', 'PUT'])
def edit2(id):
    if request.method == 'PUT':
        
        data = request.get_json(force=True)
        
        nama_pelapor = data.get('namaPelapor638')
        jenis_sampah = data.get('jenisMasalah638')
        lokasi_masalah = data.get('lokasiPermasalahan638')
        tanggal_kejadian = data.get('tanggalKejadian638')
        prioritas_penanganan = data.get('prioritas638')
        
        try:
            Model638.updateLaporan(id, nama_pelapor, jenis_sampah, lokasi_masalah, tanggal_kejadian, prioritas_penanganan)
            flash('✅ Data berhasil diperbarui.', 'success')
            return jsonify({'success': True, 'redirect': url_for('laporantabel')}), 200
        except Exception as e:
            flash(f'❌ Gagal memperbarui data: {e}', 'danger')
            return jsonify({'success': False, 'error': str(e)}), 500
    
    laporan = Model638.getLaporanById(id)
    return render_template('laporan2.html', action='Edit', laporan=laporan)

@app.route('/laporan/2')
def laporan2():
    return redirect(url_for('tambah2'))
    

@app.route('/laporantabel')
def laporantabel():
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    laporan = Model631.getLaporan(per_page, offset)
    total_data = Model631.getTotalLaporan()
    total_page = math.ceil(total_data / per_page)
    
    page2 = int(request.args.get('page2', 1))
    laporan2 = Model638.getLaporan(per_page, (page2 - 1) * per_page)
    total_data2 = Model638.getTotalLaporan()
    total_page2 = math.ceil(total_data2 / per_page)
    
    return render_template('laporantabel.html', laporan=laporan, page=page, total_page=total_page, 
                          laporan2=laporan2, page2=page2, total_page2=total_page2)

@app.route('/laporan/hapus/<int:id>', methods=['DELETE'])
def hapus(id):
    try:
        Model631.hapusLaporan(id)
        flash('✅ Data berhasil dihapus.', 'success')
        return jsonify({'success': True, 'message': 'Data berhasil dihapus'}), 200
    except Exception as e:
        flash(f'❌ Gagal menghapus data: {e}', 'danger')
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/laporan/hapus2/<int:id>', methods=['DELETE'])
def hapus2(id):
    try:
        Model638.hapusLaporan(id)
        flash('✅ Data berhasil dihapus.', 'success')
        return jsonify({'success': True, 'message': 'Data berhasil dihapus'}), 200
    except Exception as e:
        flash(f'❌ Gagal menghapus data: {e}', 'danger')
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')


if __name__ == '__main__':
    app.run(debug=True)