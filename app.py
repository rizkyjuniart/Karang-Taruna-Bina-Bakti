import streamlit as st
from pathlib import Path
import base64
from urllib.parse import quote


# =========================
# KONFIGURASI FILE
# =========================
BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "Logo Karang Taruna.png"
HERO_PATH = BASE_DIR / "hero_karang_taruna.png"
WHATSAPP_NUMBER = "6285735515920"


def gambar_ke_base64(file_path):
    try:
        file_path = Path(file_path)
        if file_path.is_file():
            return base64.b64encode(file_path.read_bytes()).decode()
        return ""
    except Exception:
        return ""


LOGO_IMAGE = gambar_ke_base64(LOGO_PATH)
HERO_IMAGE = gambar_ke_base64(HERO_PATH)

PAGE_ICON = str(LOGO_PATH) if LOGO_PATH.is_file() else "🤝"

st.set_page_config(
    page_title="Karang Taruna Bina Bakti",
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)


if HERO_IMAGE:
    HERO_BACKGROUND = f"""
        linear-gradient(
            90deg,
            rgba(4, 35, 55, 0.92),
            rgba(15, 118, 110, 0.55),
            rgba(15, 23, 42, 0.78)
        ),
        url("data:image/png;base64,{HERO_IMAGE}")
    """
else:
    HERO_BACKGROUND = "linear-gradient(135deg, #0f766e, #0f172a)"


# =========================
# CSS TAMPILAN
# =========================
st.markdown(
    f"""
    <style>
    .stApp {{
        background: #f8fafc;
    }}

    .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }}

    section[data-testid="stSidebar"] {{
        background: #eef2f7;
        border-right: 1px solid #dbe3ef;
    }}

    .sidebar-brand {{
        text-align: center;
        margin-top: 8px;
        margin-bottom: 22px;
        padding-bottom: 12px;
        border-bottom: 1px solid #dbe3ef;
    }}

    .sidebar-logo {{
        width: 135px;
        max-width: 80%;
        display: block;
        margin: 0 auto 12px auto;
    }}

    .sidebar-title-small {{
        font-size: 17px;
        font-weight: 800;
        color: #0f172a;
        margin: 0;
        line-height: 1.2;
        letter-spacing: 0.2px;
    }}

    .sidebar-title-big {{
        font-size: 30px;
        font-weight: 900;
        color: #0f172a;
        margin: 2px 0 0 0;
        line-height: 1.15;
    }}

    .sidebar-location {{
        font-size: 13px;
        font-weight: 700;
        color: #64748b;
        margin-top: 6px;
    }}

    .hero {{
        background: {HERO_BACKGROUND};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 80px 48px;
        min-height: 410px;
        border-radius: 30px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0px 22px 48px rgba(15, 23, 42, 0.22);
        display: flex;
        flex-direction: column;
        justify-content: center;
        overflow: hidden;
    }}

    .hero h1 {{
        font-size: 56px;
        line-height: 1.1;
        margin-bottom: 16px;
        color: white;
        text-shadow: 0px 5px 16px rgba(0, 0, 0, 0.55);
    }}

    .hero p {{
        font-size: 19px;
        color: #f8fafc;
        max-width: 900px;
        text-shadow: 0px 3px 10px rgba(0, 0, 0, 0.55);
        font-weight: 500;
        line-height: 1.7;
    }}

    .badge {{
        display: inline-block;
        background: rgba(245, 158, 11, 0.90);
        color: #0f172a;
        padding: 10px 17px;
        border-radius: 999px;
        font-weight: 900;
        margin-bottom: 18px;
        width: fit-content;
        box-shadow: 0px 8px 18px rgba(0, 0, 0, 0.20);
    }}

    .section-title {{
        text-align: center;
        color: #0f172a;
        margin-top: 24px;
        margin-bottom: 28px;
    }}

    .section-title p {{
        color: #0f766e;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }}

    .section-title h2 {{
        font-size: 36px;
        margin: 0;
        font-weight: 900;
    }}

    .card {{
        background: white;
        padding: 26px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.07);
        height: 100%;
    }}

    .card h3 {{
        color: #0f172a;
        margin-bottom: 10px;
        font-weight: 900;
    }}

    .card p,
    .card li {{
        color: #475569;
        font-size: 16px;
        line-height: 1.7;
    }}

    .program-card {{
        background: white;
        padding: 25px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.07);
        min-height: 205px;
        transition: 0.3s;
    }}

    .program-card:hover {{
        transform: translateY(-6px);
        border-color: #0f766e;
        box-shadow: 0px 18px 40px rgba(15, 23, 42, 0.12);
    }}

    .program-icon {{
        font-size: 42px;
        margin-bottom: 10px;
    }}

    .program-card h3 {{
        color: #0f172a;
        font-weight: 900;
        margin-bottom: 8px;
    }}

    .program-card p {{
        color: #475569;
        line-height: 1.7;
    }}

    .timeline {{
        background: white;
        padding: 25px;
        border-radius: 24px;
        border-left: 7px solid #0f766e;
        box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.07);
        height: 100%;
    }}

    .date {{
        display: inline-block;
        background: rgba(15, 118, 110, 0.12);
        color: #0f766e;
        padding: 7px 13px;
        border-radius: 999px;
        font-weight: 900;
        margin-bottom: 12px;
        font-size: 14px;
    }}

    .timeline h3 {{
        color: #0f172a;
        font-weight: 900;
    }}

    .timeline p {{
        color: #475569;
        line-height: 1.7;
    }}

    .team-card {{
        background: white;
        text-align: center;
        padding: 25px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.07);
        height: 100%;
    }}

    .avatar {{
        width: 82px;
        height: 82px;
        border-radius: 50%;
        background: linear-gradient(135deg, #0f766e, #f59e0b);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 31px;
        font-weight: 900;
        margin: 0 auto 15px auto;
        box-shadow: 0px 10px 24px rgba(15, 23, 42, 0.18);
    }}

    .team-card h3 {{
        color: #0f172a;
        font-weight: 900;
        margin-bottom: 4px;
    }}

    .team-card p {{
        color: #475569;
        font-weight: 700;
    }}

    .gallery {{
        min-height: 175px;
        border-radius: 24px;
        background:
            linear-gradient(rgba(15, 118, 110, 0.82), rgba(15, 23, 42, 0.82));
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
        font-weight: 900;
        box-shadow: 0px 12px 30px rgba(15, 23, 42, 0.12);
        margin-bottom: 18px;
    }}

    .footer {{
        background: #0f172a;
        color: #cbd5e1;
        text-align: center;
        padding: 24px;
        border-radius: 22px;
        margin-top: 42px;
        font-weight: 600;
    }}

    div[data-testid="stMetricValue"] {{
        color: #0f766e;
        font-weight: 900;
    }}

    div[data-testid="stMetricLabel"] {{
        font-weight: 800;
    }}

    @media screen and (max-width: 768px) {{
        .block-container {{
            padding: 1rem 0.9rem 1.5rem 0.9rem;
            max-width: 100%;
        }}

        section[data-testid="stSidebar"] {{
            width: min(82vw, 320px) !important;
            min-width: min(82vw, 320px) !important;
        }}

        .sidebar-brand {{
            margin-bottom: 14px;
            padding-bottom: 10px;
        }}

        .sidebar-logo {{
            width: 105px;
            margin-bottom: 10px;
        }}

        .sidebar-title-small {{
            font-size: 14px;
        }}

        .sidebar-title-big {{
            font-size: 20px;
        }}

        div[data-testid="stHorizontalBlock"] {{
            flex-wrap: wrap;
            gap: 1rem;
        }}

        div[data-testid="column"] {{
            width: 100% !important;
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }}

        .hero {{
            padding: 34px 20px;
            min-height: 360px;
            border-radius: 18px;
            margin-bottom: 18px;
            background-position: center;
        }}

        .hero h1 {{
            font-size: 34px;
            line-height: 1.12;
        }}

        .hero p {{
            font-size: 16px;
            line-height: 1.55;
        }}

        .badge {{
            font-size: 12px;
            padding: 8px 12px;
        }}

        .section-title h2 {{
            font-size: 27px;
            line-height: 1.2;
        }}

        .card,
        .program-card,
        .timeline,
        .team-card {{
            min-height: auto;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 4px;
        }}

        .card h3,
        .program-card h3,
        .timeline h3,
        .team-card h3 {{
            font-size: 22px;
            line-height: 1.2;
            word-break: normal;
            overflow-wrap: normal;
        }}

        .card p,
        .card li,
        .program-card p,
        .timeline p {{
            font-size: 15px;
            line-height: 1.65;
        }}

        .footer {{
            padding: 18px;
            border-radius: 16px;
            margin-top: 26px;
            font-size: 13px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# FUNGSI KOMPONEN
# =========================
def section_title(label, title):
    st.markdown(
        f"""
        <div class="section-title">
            <p>{label}</p>
            <h2>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card(title, text):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def program_card(icon, title, text):
    st.markdown(
        f"""
        <div class="program-card">
            <div class="program-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# SIDEBAR
# =========================
if LOGO_IMAGE:
    sidebar_logo_html = f'<img class="sidebar-logo" src="data:image/png;base64,{LOGO_IMAGE}" alt="Logo Karang Taruna">'
else:
    sidebar_logo_html = """
    <div style="font-size:72px; text-align:center;">🤝</div>
    """

st.sidebar.markdown(
    f"""<div class="sidebar-brand">
{sidebar_logo_html}
<p class="sidebar-title-small">Karang Taruna</p>
<p class="sidebar-title-big">Bina Bakti</p>
<p class="sidebar-location">Kelurahan Banjarmlati</p>
</div>""",
    unsafe_allow_html=True,
)

menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "Beranda",
        "Profil",
        "Program Kerja",
        "Kegiatan",
        "Pengurus",
        "Galeri",
        "Kontak",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Karang Taruna Bina Bakti Kelurahan Banjarmlati sebagai wadah pemuda aktif, kreatif, dan peduli sosial."
)


# =========================
# HALAMAN BERANDA
# =========================
if menu == "Beranda":
    st.markdown(
        """
        <div class="hero">
            <span class="badge">Karang Taruna Kelurahan Banjarmlati</span>
            <h1>Karang Taruna Bina Bakti</h1>
            <p>
                Generasi muda aktif, kreatif, dan peduli sosial untuk membangun lingkungan
                Kelurahan Banjarmlati yang lebih maju, kompak, dan bermanfaat bagi masyarakat.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Anggota Aktif", "25+")
    col2.metric("Program Sosial", "10+")
    col3.metric("Kegiatan Tahunan", "5+")
    col4.metric("Tujuan Bersama", "1")

    st.write("")
    section_title("Tentang Organisasi", "Kenapa Karang Taruna Itu Penting?")

    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "Wadah Pemuda",
            "Menjadi tempat bagi pemuda untuk belajar organisasi, kerja sama, dan kepemimpinan.",
        )

    with c2:
        card(
            "Peduli Masyarakat",
            "Mendorong kegiatan sosial yang bermanfaat bagi warga dan lingkungan sekitar.",
        )

    with c3:
        card(
            "Kreatif dan Produktif",
            "Mengembangkan bakat, minat, kreativitas, dan potensi generasi muda.",
        )


# =========================
# HALAMAN PROFIL
# =========================
elif menu == "Profil":
    section_title("Profil", "Karang Taruna Bina Bakti")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>Wadah Kreativitas dan Pengabdian Pemuda</h3>
                <p>
                    Karang Taruna Bina Bakti Kelurahan Banjarmlati merupakan organisasi
                    kepemudaan yang bergerak di bidang sosial kemasyarakatan.
                    Organisasi ini menjadi tempat bagi generasi muda untuk mengembangkan
                    potensi, kepemimpinan, solidaritas, dan kepedulian terhadap lingkungan.
                </p>
                <p>
                    Melalui berbagai kegiatan, Karang Taruna Bina Bakti berupaya menciptakan
                    pemuda yang mandiri, produktif, dan mampu memberikan manfaat nyata
                    bagi masyarakat Kelurahan Banjarmlati.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>Visi</h3>
                <p>
                    Mewujudkan pemuda Banjarmlati yang aktif, kreatif, berdaya saing,
                    dan peduli terhadap kehidupan sosial masyarakat.
                </p>

                <h3>Misi</h3>
                <ul>
                    <li>Meningkatkan partisipasi pemuda dalam kegiatan sosial.</li>
                    <li>Mengembangkan bakat, minat, dan kreativitas anggota.</li>
                    <li>Menumbuhkan semangat gotong royong.</li>
                    <li>Mendukung program kelurahan dalam pemberdayaan masyarakat.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================
# HALAMAN PROGRAM KERJA
# =========================
elif menu == "Program Kerja":
    section_title("Program Kerja", "Program Unggulan Bina Bakti")

    p1, p2, p3 = st.columns(3)

    with p1:
        program_card(
            "🌱",
            "Peduli Lingkungan",
            "Kerja bakti, penghijauan, dan kampanye kebersihan lingkungan.",
        )

    with p2:
        program_card(
            "⚽",
            "Olahraga Pemuda",
            "Turnamen dan latihan bersama untuk mempererat persaudaraan.",
        )

    with p3:
        program_card(
            "🎨",
            "Seni dan Kreativitas",
            "Mengembangkan kreativitas melalui seni, desain, musik, dan budaya.",
        )

    st.write("")

    p4, p5, p6 = st.columns(3)

    with p4:
        program_card(
            "🤲",
            "Bakti Sosial",
            "Kegiatan sosial, donasi, dan aksi kemanusiaan untuk masyarakat.",
        )

    with p5:
        program_card(
            "💼",
            "Kewirausahaan",
            "Pelatihan usaha kecil, digital marketing, dan ekonomi pemuda.",
        )

    with p6:
        program_card(
            "📚",
            "Edukasi Pemuda",
            "Pelatihan teknologi, pembelajaran, dan peningkatan wawasan pemuda.",
        )


# =========================
# HALAMAN KEGIATAN
# =========================
elif menu == "Kegiatan":
    section_title("Agenda", "Kegiatan Terbaru")

    k1, k2, k3 = st.columns(3)

    with k1:
        st.markdown(
            """
            <div class="timeline">
                <span class="date">Januari 2026</span>
                <h3>Rapat Koordinasi Anggota</h3>
                <p>Pembahasan program kerja tahunan dan pembagian tugas pengurus.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k2:
        st.markdown(
            """
            <div class="timeline">
                <span class="date">Maret 2026</span>
                <h3>Kerja Bakti Lingkungan</h3>
                <p>Aksi bersih lingkungan bersama warga sekitar Kelurahan Banjarmlati.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with k3:
        st.markdown(
            """
            <div class="timeline">
                <span class="date">Agustus 2026</span>
                <h3>Lomba Kemerdekaan</h3>
                <p>Kegiatan perlombaan 17 Agustus untuk anak-anak, remaja, dan masyarakat.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================
# HALAMAN PENGURUS
# =========================
elif menu == "Pengurus":
    section_title("Struktur Organisasi", "Pengurus Karang Taruna")

    st.warning("Silakan ganti nama pengurus sesuai data asli organisasi.")

    t1, t2, t3, t4 = st.columns(4)

    data_pengurus = [
        ("K", "Ketua", "Nama Ketua"),
        ("W", "Wakil Ketua", "Nama Wakil Ketua"),
        ("S", "Sekretaris", "Nama Sekretaris"),
        ("B", "Bendahara", "Nama Bendahara"),
    ]

    for col, item in zip([t1, t2, t3, t4], data_pengurus):
        huruf, jabatan, nama = item

        with col:
            st.markdown(
                f"""
                <div class="team-card">
                    <div class="avatar">{huruf}</div>
                    <h3>{jabatan}</h3>
                    <p>{nama}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================
# HALAMAN GALERI
# =========================
elif menu == "Galeri":
    section_title("Dokumentasi", "Galeri Kegiatan")

    g1, g2, g3 = st.columns(3)

    with g1:
        st.markdown('<div class="gallery">Kerja Bakti</div>', unsafe_allow_html=True)
        st.markdown('<div class="gallery">Rapat Anggota</div>', unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="gallery">Bakti Sosial</div>', unsafe_allow_html=True)
        st.markdown('<div class="gallery">Olahraga</div>', unsafe_allow_html=True)

    with g3:
        st.markdown('<div class="gallery">Lomba Pemuda</div>', unsafe_allow_html=True)
        st.markdown('<div class="gallery">Pelatihan</div>', unsafe_allow_html=True)


# =========================
# HALAMAN KONTAK
# =========================
elif menu == "Kontak":
    section_title("Kontak", "Hubungi Karang Taruna Bina Bakti")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>Mari Bergabung dan Bergerak Bersama</h3>
                <p>
                    Hubungi Karang Taruna Bina Bakti untuk informasi kegiatan,
                    kerja sama, atau pendaftaran anggota baru.
                </p>
                <p><b>Alamat:</b> Kelurahan Banjarmlati</p>
                <p><b>Email:</b> binabakti@karangtaruna.id</p>
                <p><b>WhatsApp:</b> 0857-3551-5920 (Mas Heri)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        with st.form("form_kontak"):
            nama = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            pesan = st.text_area("Pesan")
            kirim = st.form_submit_button("Kirim Pesan")

            if kirim:
                if nama and email and pesan:
                    isi_whatsapp = f"""Halo Karang Taruna Bina Bakti,

Saya ingin menghubungi lewat website.

Nama: {nama}
Email: {email}
Pesan: {pesan}"""
                    st.session_state["whatsapp_link"] = (
                        f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(isi_whatsapp)}"
                    )
                    st.success(f"Terima kasih, {nama}. Pesan Anda berhasil dibuat.")
                else:
                    st.session_state.pop("whatsapp_link", None)
                    st.error("Mohon lengkapi semua data terlebih dahulu.")

        if "whatsapp_link" in st.session_state:
            st.link_button(
                "Kirim Pesan ke WhatsApp",
                st.session_state["whatsapp_link"],
                use_container_width=True,
            )


# =========================
# FOOTER
# =========================
st.markdown(
    """
    <div class="footer">
        © 2026 Karang Taruna Bina Bakti Kelurahan Banjarmlati. Semua Hak Dilindungi.
    </div>
    """,
    unsafe_allow_html=True,
)
