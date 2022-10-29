
import Image from "next/image";
import Link from "next/link";

const Card = ({source,title,desc,path}) => {
  return (
    <Link href={`/admin/${path}`}>
    <div className="bg-white w-48 text-center p-7 space-y-0.5 rounded-lg shadow-md hover:scale-110 hover:shadow-lg transition-transform cursor-pointer">
      {/* icon */}
     <Image src={source} height={50} width={60} alt="logo"/>
      {/* title */}
      <h1 className="text-xl font-bold">{title}</h1>
      {/* description */}
      <p className="text-gray-400 text-xs">{desc}</p>
    </div>
    </Link>
  );
};

export default Card;
