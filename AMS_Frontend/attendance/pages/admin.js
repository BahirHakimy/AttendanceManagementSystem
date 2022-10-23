import Link from "next/link";
import Image from "next/image";
import classIcon from "../public/class.png";
import studentIcon from "../public/student.png";
import teacherIcon from "../public/teacher.png";
import subjectIcon from "../public/subject.png";

const Admin = () => {
  return (
    <div className="p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4 gap-5">
      {/* class card */}
      <Link href="/class">
        <div className="rounded overflow-hidden shadow-2xl bg-gray-100 hover:bg-gray-200 cursor-pointer">
          <Image className="max-w-xs h-auto" src={classIcon} alt="User" />
          <div>
            <p className="font-bold text-xl text-center uppercase">Classes</p>
          </div>
        </div>
      </Link>

      {/* student card */}
      <Link href="/student">
        <div className="rounded overflow-hidden shadow-xl bg-gray-100 hover:bg-gray-200 cursor-pointer">
          <Image
            className="w-full  object-cover"
            src={studentIcon}
            alt="User"
          />
          <div className="mb-2">
            <p className="font-bold text-xl text-center uppercase">Students</p>
          </div>
        </div>
      </Link>

      {/* teacher card */}
      <Link href="/teacher">
        <div className="rounded overflow-hidden shadow-xl bg-gray-100 hover:bg-gray-200 cursor-pointer">
          <Image
            className="w-full  object-cover"
            src={teacherIcon}
            alt="User"
          />
          <div className="mb-2">
            <p className="font-bold text-xl text-center uppercase">Teachers</p>
          </div>
        </div>
      </Link>

      {/* subject card */}
      <Link href="/subject">
        <div className="rounded overflow-hidden shadow-xl bg-gray-100 hover:bg-gray-200 cursor-pointer">
          <Image className="w-full object-cover" src={subjectIcon} alt="User" />
          <div className="mb-2">
            <p className="font-bold text-xl text-center uppercase">Subjects</p>
          </div>
        </div>
      </Link>
    </div>
  );
};

export default Admin;
