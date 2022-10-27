import { BiArrowBack } from "react-icons/bi";
import Image from "next/image";
import KuLogo from "../public/KuLogo.jpg";
import { Formik, Form, Field } from "formik";
import { FcSearch } from "react-icons/fc";

const TeacherDisplayPanel = () => {
  return (
    <div className="grow mx-8">
      {/* logo of university and back button  */}
      <div className="flex items-center justify-between mt-5">
        <BiArrowBack size={25} className="text-cyan-600 cursor-pointer" />
        <Image src={KuLogo} height={80} width={80} alt="Kabul University" />
      </div>
      {/* title  */}
      <div>
        <h1 className="text-2xl font-bold italic pb-2">Teachers Panel</h1>
        {/* //todo to change the thickness */}
        <hr />
      </div>
      {/* search bar  */}
      <div className="text-end relative">
        {/* input field */}
        <Formik initialValues={{searchValue : ''}}>
          <Form>
            {/* <label htmlFor="searchValue"></label> */}
            <div className="mt-5">
              <FcSearch className="absolute  h-10 rounded right-52 " size={25} />
              <Field
                type="text"
                className=" rounded-lg border-darkShadeCyan border-2 mr-2 pl-10 focus:ring-cyan-400 focus:border-cyan-400 placeholder:text-xs placeholder:text-gray-400  "
                name="searchValue"
                placeholder="Search through Id or Name"
              />
            </div>
          </Form>
        </Formik>
      </div>
      {/* showing the data in table  */}
    </div>
  );
};

export default TeacherDisplayPanel;

// data must be in link mode
// search shown in card
// maybe types of sort
// search through what
// id must be changed to something meaningful
