
import Navbar from "../../components/navbar";
import DisplayPanel from "../../components/adminDisplayPanel";



const Admin = () => {
  return (
    <div className="bg-slate-50 h-screen flex">
      {/* navbar */}
      <Navbar />
      {/* display panel */}
      <DisplayPanel/>
    </div>
  );
};

export default Admin;
