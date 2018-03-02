import {auth as dev} from './config.dev';
import {auth as prod} from './config.prod';

const isProd = () => process.env.NODE_ENV === 'production' ? true : false;
const config = isProd() ? prod : dev;
export default config;