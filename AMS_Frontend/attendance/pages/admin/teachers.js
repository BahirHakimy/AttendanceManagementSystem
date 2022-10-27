import Navbar from "../../components/navbar";
import TeacherDisplayPanel from "../../components/teachersDisplayPanel";

const TeacherPanel = () => {
  return (
    <div className="flex">
      {/* navbar  */}
      <Navbar />
      {/* teachers display panel  */}
      <TeacherDisplayPanel/>
    </div>
  );
};

export default TeacherPanel;
