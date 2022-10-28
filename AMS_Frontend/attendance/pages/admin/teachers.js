import Navbar from "../../components/navbar";
import TeacherDisplayPanel from "../../components/teachersDisplayPanel";
import axios from "axios";

const TeacherPanel = ({ data }) => {
  return (
    <div className="flex">
      {/* navbar  */}
      <Navbar />
      {/* teachers display panel  */}
      <TeacherDisplayPanel data={data} />
    </div>
  );
};

export default TeacherPanel;

export async function getStaticProps(context) {
  let data = {};
  await axios
    .get("http://127.0.0.1:8000/api/users/get-teachers/")
    .then((res) => {
      data = {
        info : res.data.teachers,
        status : res.status
      }
    });

  return {
    props: {
      data,
    }, // will be passed to the page component as props
  };
}
