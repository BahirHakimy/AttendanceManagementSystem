import Image from "next/image";
import Link from "next/link";
import classIcon from "../public/Classroom.svg";
import subjectIcon from "../public/book.svg";
import teacherIcon from "../public/teacher.svg";
import studentIcon from "../public/student.svg";
import ku4Admin from "../public/ku4Admin.svg";

const Navbar = () => {
  return (
    <div className=" pt-10 bg-darkShadeCyan flex flex-col gap-6 w-48 h-screen items-center  ">
      {/*logo*/}
      <div className="bg-white p-2 rounded-lg mb-4">
        <Image src={ku4Admin} height={30} width={90} alt="logo" />
      </div>
      {/* subjects  */}
      <Link href={"/"}>
        <a className="flex items-center text-white gap-5 w-full  hover:bg-cyan-500 px-3 py-1 ">
          <Image src={subjectIcon} height={40} width={40} />
          <span>Subjects Panel</span>
        </a>
      </Link>

      {/* Classroom */}
      <Link href={"/"}>
        <a className="flex items-center text-white gap-5 w-full hover:bg-cyan-500 px-3 py-1 ">
          <Image src={classIcon} height={40} width={40} />
          <span>Classes Panel</span>
        </a>
      </Link>

      {/* Students */}
      <Link href={"/"}>
        <a className="flex items-center text-white gap-5 w-full hover:bg-cyan-500 px-3 py-1 ">
          <Image src={studentIcon} height={40} width={40} />
          <span>Students Panel</span>
        </a>
      </Link>

      {/* teachers */}
      <Link href={"/"}>
        <a className="flex items-center text-white gap-5 w-full hover:bg-cyan-500 px-3 py-1">
          <Image src={teacherIcon} height={40} width={40} />
          <span>Teachers Panel</span>
        </a>
      </Link>
    </div>
  );
};

export default Navbar;
