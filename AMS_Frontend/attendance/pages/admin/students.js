import Navbar from "../../components/navbar"
import StudentsDisplayPanel from "../../components/StudentsDisplayPanelCompnent"

const StudentsPanel = () => {
  return (
    <div className="flex">
        {/* navbar */}
        <Navbar/>
        {/* Students Display Panel */}
        <StudentsDisplayPanel/>
    </div>
  )
}

export default StudentsPanel


export async function getStaticProps() {
  let data = {};
  await axios
    .get("http://127.0.0.1:8000/api/users/get-students/")
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