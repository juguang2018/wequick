<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateFriendsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('friends', function (Blueprint $table) {
            $table->increments('id');
            $table->string('cwxid',255)->nullable(false)->comment('登陆微信号');
            $table->string('wxid',255)->nullable(false);
            $table->string('nick',255)->nullable()->comment('昵称');
            $table->string('username',255)->nullable()->comment('微信账号 用户设置的');
            $table->string('asName',255)->nullable()->comment('备注名');
            $table->string('headPic',255)->nullable()->comment('头像');
            $table->tinyInteger('sex')->default(1)->comment('性别');
            $table->string('nationality',255)->nullable()->comment('国籍');
            $table->string('province',255)->nullable()->comment('省份');
            $table->string('city',255)->nullable()->comment('城市');
            $table->tinyInteger('type')->default(1)->comment('类型 1个人号 2群 3公众号');
            $table->tinyInteger('groupId')->nullable()->comment('如果是群成员，这个字段用来放群id');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('friends');
    }
}
