import { Field, Form, Formik } from "formik";
import Image from "next/image";
import React from "react";
import { BiArrowBack } from "react-icons/bi";
import {
  BsCardList,
  BsFillPersonLinesFill,
  BsPersonPlusFill,
} from "react-icons/bs";
import { FcSearch } from "react-icons/fc";
import KuLogo from "../public/KuLogo.jpg";

const StudentsDisplayPanel = () => {
  return (
    <div className="grow mx-8">
      {/* Arrow to back and Ku Logo */}
      <div className="flex items-center justify-between mt-5">
        <BiArrowBack size={25} className="text-cyan-600 cursor-pointer" />
        <Image src={KuLogo} height={80} width={80} alt="Kabul University" />
      </div>
      {/* title  */}
      <div>
        <h1 className="text-2xl font-bold italic pb-2">Students Panel</h1>
        {/* //todo to change the thickness */}
        <hr />
      </div>
      {/* second row contains the search bar the filter buttons   */}
      <div className="flex  justify-between mb-2 ">
        {/* search bar  */}
        <div className="flex items-center relative order-2">
          <BsPersonPlusFill size={20} className="" />
          {/* input field */}
          <Formik initialValues={{ searchValue: "" }}>
            <Form>
              {/* <label htmlFor="searchValue"></label> */}
              <div className="mt-5">
                <FcSearch
                  className="absolute bottom-3 rounded right-52 "
                  size={25}
                />
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
        <div className="mt-8 mr-2 ">
          {/* table title */}
          <div className="flex items-center mb-1 gap-4">
            <h1 className="font-semibold text-lg">The Students List</h1>
            {/* view filter */}
            <div className="flex gap-4">
              <BsCardList
                title="List"
                size={30}
                className=""
                onClick={() => setTypeOfView(false)}
              />
              <BsFillPersonLinesFill
                size={30}
                className="hover:text-gray-400"
                onClick={() => setTypeOfView(true)}
              />
            </div>
          </div>
        </div>
      </div>
      <hr />
    </div>
  );
};

export default StudentsDisplayPanel;
