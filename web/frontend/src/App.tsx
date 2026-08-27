import { NavLink, Route, Routes } from "react-router-dom";
import BrowsePage from "./pages/BrowsePage";
import DetailPage from "./pages/DetailPage";
import UploadPage from "./pages/UploadPage";

export default function App() {
  return (
    <div className="shell">
      <header className="topnav">
        <div className="brand">
          <strong>Skill 数据集门户</strong>
          <span>全部数据集 · security_merged_v1 + skills_relational_v1</span>
        </div>
        <nav className="nav-links">
          <NavLink to="/" end>
            浏览
          </NavLink>
          <NavLink to="/upload">上传</NavLink>
          <a href="/api/dataset/download">下载数据集</a>
        </nav>
      </header>
      <Routes>
        <Route path="/" element={<BrowsePage />} />
        <Route path="/skill/:id" element={<DetailPage />} />
        <Route path="/upload" element={<UploadPage />} />
      </Routes>
    </div>
  );
}
