import { BiArrowBack } from "react-icons/bi";
import Image from "next/image";
import KuLogo from "../public/KuLogo.jpg";
import { Formik, Form, Field } from "formik";
import { FcSearch } from "react-icons/fc";
import { BsCardList, BsFillPersonLinesFill } from "react-icons/bs";
import { useState } from "react";
import TableCellMaker from "./TableCellMakerComponent";
import CardTypeCellMaker from "./cardTypeCellMaker";

const TeacherDisplayPanel = ({ data }) => {
  const [typeOfViewCard, setTypeOfView] = useState(false);

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
      {/* second row contains the search bar the filter buttons   */}
      <div className="flex justify-between mb-2 ">
        {/* search bar  */}
        <div className=" relative order-2">
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
            <h1 className="font-semibold text-lg">The Mentors List</h1>
            {/* view filter */}
            <div className="flex gap-4">
              <BsCardList
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
      {/* THe table or the card  */}
      {/* if typeofViewnCArd is true then the list will be shown in card if not then it is list */}
      {typeOfViewCard ? (
        <div>
          {data.info.map((cell) => (
            <CardTypeCellMaker key={cell.user.id} cellData={cell} />
          ))}
        </div>
      ) : (
        <div className="border border-black rounded mt-10 w-3/4 mx-auto ">
          <table className="w-full table-auto ">
            <thead className="border-black border-b">
              <tr>
                <th>No:</th>
                <th>Username</th>
                <th>Name</th>
                <th>Last Name</th>
                <th>Degree</th>
              </tr>
            </thead>
            <tbody className="text-center">
              {data.info.map((cell, idx) => (
                <TableCellMaker key={cell.user.id} cellData={cell} idx={idx} />
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default TeacherDisplayPanel;

// data must be in link mode
// search shown in card
// maybe types of sort
// search through what
// id must be changed to something meaningful
// the directory must be changed
