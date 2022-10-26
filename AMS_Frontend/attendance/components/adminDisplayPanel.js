import bookColored from "../public/bookColored.svg";
import classroomColored from "../public/classroomColored.svg";
import Image from "next/image";
import ku4Title from "../public/adminTitle.svg";
import Card from "./cardMaker";
import studentColored from "../public/studentColored.svg";
import teacherColored from "../public/teacher.png";
const DisplayPanel = () => {
  return (
    <div className=" grow">
      {/* title */}
      {/* //todo right now as a image but to be changed to real html */}
      <div className="flex justify-center ">
        <Image src={ku4Title} width={700} alt="title" />
      </div>
      {/* cards  */}
      <div className="pl-10 pr-10">
        {/* facility title */}
        <h1 className="font-semibold text-gray-400">The Portal Facilities</h1>
        <hr />
        {/* Subjects and classroom  */}
        <div className="flex justify-center gap-4 mt-7">
          {/* Subjects Card */}
          <Card
            source={bookColored}
            title="Subjects Panel"
            desc="Add, Delete or Update Subjects"
          />

          <Card
            source={classroomColored}
            title="Classroom Panel"
            desc="See through Classes and control them"
          />
        </div>
        {/* student and teacher */}
        <div className="flex justify-center mt-5 gap-4">
          {/* student Card */}
          <Card
            source={studentColored}
            title="Students Panel"
            desc="Manage and Search through Student list"
          />
          {/* teacher Card */}
          <Card
            source={teacherColored}
            title="Teachers Panel"
            desc="Manage and Search through Teachers list"
          />
        </div>
      </div>
    </div>
  );
};

export default DisplayPanel;
