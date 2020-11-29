import React from 'react';
import {Layout, Menu, Avatar} from 'antd';
import {Link} from 'react-router-dom';
import {HeartFilled, UserOutlined} from '@ant-design/icons';
import './Header.scss';

const Header = () => {
  return (
    <Layout.Header className="header">
      <div className="logo">
        <HeartFilled style={{ color: 'hotpink' }} />
        &nbsp;
        Сердце
      </div>
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
        <Menu.Item key="1">
          <Link to="/">Анкеты</Link>
        </Menu.Item>
        <Menu.Item key="2">
          <Link to="/train">Тренажер</Link>
        </Menu.Item>
        <Menu.Item key="3">
          <Link to="/med">Аналитика</Link>
        </Menu.Item>
      </Menu>
      <div className="user">
        <Avatar icon={<UserOutlined />} />
        &nbsp;
        Елена
      </div>
    </Layout.Header>
  );
};

export default Header;
