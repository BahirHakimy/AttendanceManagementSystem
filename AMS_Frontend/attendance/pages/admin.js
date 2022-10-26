import Link from "next/link";
import Image from "next/image";
// import classNameIcon from "../public/class.png";
// import studentIcon from "../public/student.png";
// import teacherIcon from "../public/teacher.png";
// import subjectIcon from "../public/subject.png";

import { SiGoogleclassroom } from "react-icons/si";
import { FaChalkboardTeacher } from "react-icons/fa";
import { GiTeacher } from "react-icons/gi";
import { MdSubject } from "react-icons/md";
import { TbLayoutDashboard } from "react-icons/tb";
import { BiLogOut } from "react-icons/bi";

const Admin = () => {
  return (
    <div className="flex">
      {/* sidebar */}
      <aside className="w-64" aria-label="Sidebar">
        <div className="h-screen overflow-y-auto py-4 px-3 bg-gray-50 dark:bg-gray-800">
          <ul className="space-y-2">
            <li>
              <Link href="/dashboard">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <TbLayoutDashboard className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">
                    Dashboard
                  </span>
                </div>
              </Link>
            </li>
            <li>
              <Link href="/class">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <SiGoogleclassroom className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">classes</span>
                </div>
              </Link>
            </li>
            <li>
              <Link href="/student">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <FaChalkboardTeacher className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">student</span>
                </div>
              </Link>
            </li>
            <li>
              <Link href="/teacher">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <GiTeacher className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">teacher</span>
                </div>
              </Link>
            </li>
            <li>
              <Link href="/subject">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <MdSubject className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">subject</span>
                </div>
              </Link>
            </li>
            <li>
              <Link href="/log-out">
                <div className="flex items-center p-2 font-normal rounded-lg text-orange-600 uppercase text-xl  hover:bg-gray-100 dark:hover:bg-gray-700 cursor-pointer">
                  <BiLogOut className="text-3xl" />
                  <span className="flex-1 ml-3 whitespace-nowrap">Log Out</span>
                </div>
              </Link>
            </li>
          </ul>
        </div>
      </aside>

      {/* main cards */}
      <div className="w-full bg-gray-600">
        <h1 className="text-center text-3xl mt-10 text-gray-100">
          Attendance Management System
        </h1>
        <div className="mx-auto max-w-xl p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-5">
          {/* className card */}
          <Link href="/className">
            <div className="w-62 h-48 pt-5 rounded overflow-hidden shadow-black shadow-2xl bg-gray-800 hover:bg-gray-700 cursor-pointer text-gray-300">
              <div className="text-9xl flex justify-center">
                <SiGoogleclassroom />
              </div>
              <p className="font-bold text-xl text-center uppercase mt-2">
                classes
              </p>
            </div>
          </Link>

          {/* student card */}
          <Link href="/className">
            <div className="w-62 h-48 pt-5 rounded overflow-hidden shadow-black shadow-2xl bg-gray-100 hover:bg-gray-300 cursor-pointer text-orange-600">
              <div className="text-9xl flex justify-center">
                <FaChalkboardTeacher />
              </div>
              <p className="font-bold text-xl text-center uppercase mt-2">
                students
              </p>
            </div>
          </Link>

          {/* teacher card */}
          <Link href="/className">
            <div className="w-62 h-48 pt-5 rounded overflow-hidden shadow-black shadow-2xl bg-gray-100 hover:bg-gray-300 cursor-pointer text-orange-600">
              <div className="text-9xl flex justify-center">
                <GiTeacher />
              </div>
              <p className="font-bold text-xl text-center uppercase mt-2">
                teachers
              </p>
            </div>
          </Link>

          {/* subject card */}
          <Link href="/className">
            <div className="w-62 h-48 pt-5 rounded overflow-hidden shadow-black shadow-2xl bg-gray-800 hover:bg-gray-700 cursor-pointer text-gray-300">
              <div className="text-9xl flex justify-center">
                <MdSubject />
              </div>
              <p className="font-bold text-xl text-center uppercase mt-2">
                subjects
              </p>
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Admin;
