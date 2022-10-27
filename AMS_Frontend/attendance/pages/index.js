import { Formik, Form, Field } from "formik";
import Image from "next/image";
import ku4 from "../public/ku4.svg";
const Index = () => {
  const handleSubmit = () => {};

  return (
    <div>
      <div className="flex justify-center items-center h-screen">
        {/* the svg and the text */}
        <div className="">
          <Image src={ku4} alt="logo" height={60} />
          <p></p>
          <p className="text-2xl w-1/2 mt-3 mx-auto font-bold capitalize text-gray-400 italic">
            kabul universities &nbsp; &nbsp;online portal
          </p>
        </div>
        {/*  vertical line  */}
        <div className="border border-blue-700 h-96"></div>
        {/* the form and the button */}
        <div className="px-20">
          <Formik
            onSubmit={handleSubmit}
            initialValues={{ username: "", password: "" }}
          >
            <Form>
              {/* username */}
              <div>
                <Field
                  name="username"
                  type="text"
                  className="form-input "
                  placeholder="Username"
                />
              </div>
              {/* password */}
              <div>
                <Field
                  name="password"
                  className="form-input"
                  type="password"
                  placeholder="password"
                />
              </div>
              {/* button */}
              <div>
                <button
                  type="submit"
                  className="bg-indigo-500 text-white w-72 h-10 rounded-lg"
                >
                  Log In
                </button>
                <p className="text-gray-400">forgot password?</p>
              </div>
            </Form>
          </Formik>
        </div>
      </div>
    </div>
  );
};

export default Index;
