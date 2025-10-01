import streamlit as st

# -------------------------------
# Profile Page (หน้า 1)
# -------------------------------
st.title("👨‍🎓 Profile Page")

# Layout สองคอลัมน์
col1, col2 = st.columns([1, 2])

with col2:
    st.subheader("แนะนำตัวเอง")
    st.write("**ชื่อ:** ศรัณย์กร วชรกุล")
    st.write("**รหัสนักศึกษา:** 2313310191")
    st.write("**สาขา:** Digital Business Information Technology")

# ความสนใจ
st.header("🎯 ความสนใจ (Interest in Data Science / Data Mining)")
st.write("""
- สนใจการใช้ข้อมูลเพื่อค้นหาความสัมพันธ์และสร้างคุณค่าใหม่ ๆ  
- ชอบการทำ Visualization ให้เข้าใจง่ายและนำไปใช้ตัดสินใจได้จริง  
- อยากพัฒนาทักษะ Machine Learning เพื่อสร้างโมเดลพยากรณ์  
- เป้าหมายคือการนำ Data Science ไปใช้ในธุรกิจและงานวิจัย  
""")

# ประสบการณ์
st.header("📌 ประสบการณ์ที่เกี่ยวข้อง (Experiences / Projects)")

st.subheader("1. Dashboard วิเคราะห์ข้อมูล Billionaire 2025")
st.write("""
- ใช้ Power BI / Visualization Tools (Pie Chart, Bar Chart, Map)  
- วิเคราะห์ข้อมูลตาม Generation, Industry, Country  
""")

st.subheader("2. Mini Project: ERP Workflow (Pharmacy Sales Process)")
st.write("""
- **Objective:** เชื่อมโยงกระบวนการ  
  → สั่งซื้อยา → ตรวจสอบสต็อก → อัปเดตสต็อก → บันทึกยอดขาย → ออกใบเสร็จ  
- **Role:** Business Analyst + ออกแบบ Activity Diagram  
- **Tools:** Draw.io, PowerPoint, ERP Concepts (Sales, Inventory, POS, Finance)  
- **Outcome:** ได้ Process Diagram ที่ใช้เป็น Requirement ให้ทีม ERP  
  → ลดความซ้ำซ้อน และระบุ Integration Points ชัดเจน  
""")

# ทักษะ
st.header("🛠️ Skillset & Tools")
st.write("""
- **Programming:** Python, SQL, Java  
- **Visualization:** Power BI, SAP  
- **Others:** Microsoft Word, Excel, PowerPoint  
""")








